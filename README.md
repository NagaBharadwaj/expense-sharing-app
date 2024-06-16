# Expense Sharing App

An Expense Sharing App built with Python and Flask. This app allows users to create groups, add expenses, and track who owes whom.

## Features

- Create groups
- Add expenses to groups
- View all expenses in a group
- Track who owes whom

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/NagaBharadwaj/expense-sharing-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd expense-sharing-app
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Initialize the SQLite database:
    ```bash
    python init_db.py
    ```
7. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Add a new group by entering the group name and clicking "Add Group".
3. Click on the group name to view the group's expenses.
4. Add an expense to the group by clicking "Add Expense" and filling out the form.

## Project Structure
expense_app/
├── app.py
├── init_db.py
├── templates/
│ ├── index.html
│ ├── add_expense.html
│ └── group.html
├── static/
│ └── style.css
└── data/
└── database.db
