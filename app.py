from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'data/database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM groups")
    groups = cur.fetchall()
    conn.close()
    return render_template('index.html', groups=groups)

@app.route('/add_group', methods=['POST'])
def add_group():
    group_name = request.form['group_name']
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/group/<int:group_id>')
def group(group_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses WHERE group_id = ?", (group_id,))
    expenses = cur.fetchall()
    cur.execute("SELECT name FROM groups WHERE id = ?", (group_id,))
    group_name = cur.fetchone()[0]
    conn.close()
    return render_template('group.html', group_name=group_name, expenses=expenses, group_id=group_id)

@app.route('/group/<int:group_id>/add_expense', methods=['GET', 'POST'])
def add_expense(group_id):
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO expenses (group_id, description, amount) VALUES (?, ?, ?)", (group_id, description, amount))
        conn.commit()
        conn.close()
        return redirect(url_for('group', group_id=group_id))
    return render_template('add_expense.html', group_id=group_id)

if __name__ == '__main__':
    app.run(debug=True)
