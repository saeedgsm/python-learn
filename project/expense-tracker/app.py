import sqlite3
from datetime import datetime

DB_PATH= "./project/expense-tracker/expenses.db"

def execute_query(query,params=(),fetch=False):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query,params)
            if fetch:
                return cursor.fetchall()
            else:
                return cursor.lastrowid
    except sqlite3.Error as e:
        print("DATABASE ERROR!")
        return None


def create_db():
    query = """
                CREATE TABLE IF NOT EXISTS expenses (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL CHECK(length(title) <= 50),
                       amount REAL NOT CHECK(amount > 0),
                       category TEXT NOT NULL CHECK(length(category) <=30),
                       date TEXT NOT NULL
                       )
                    """
    execute_query(query)
    print("Database and table created!")

def add(title,amount,category):
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = """
        INSERT INTO expenses (title, amount, category, date)
        VALUES(?,?,?,?)
        """
    expense_id = execute_query(query,(title,amount,category,date_now))
    if expense_id:
        print(f"expense : {title} by id = {expense_id} saved!")


def get_all():
    query = "SELECT id,title, amount, category, date FROM expenses ORDER BY date DESC"
    rows = execute_query(query,fetch=True)
    print("Expenses List: \n")
    for row in rows:
        print(f"ID:{row[0]} | {row[1]} | {row[2]} $ | {row[3]} | {row[4]}")
    print("-" * 40)
    return rows


def total_expenses():
    query="SELECT SUM(amount) FROM expenses"
    result = execute_query(query,fetch=True)
    total = result[0][0] if result and result[0][0] else 0
    print(f"total expenses: {total} $")
    return total

def total_by_category():
    query = """
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    ORDER BY SUM(amount) DESC
    """
    rows = execute_query(query, fetch=True)
    print("\n📊 total expenses by category:")
    for row in rows:
        print(f"{row[0]}: {row[1]} $")
    return rows

def max_expense():
    query = "SELECT title, amount, category, date FROM expenses ORDER BY amount DESC LIMIT 1"
    row = execute_query(query, fetch=True)
    if row:
        print(f"\n🏆 max expense: {row[0][0]} | {row[0][1]} $ | {row[0][2]} | {row[0][3]}")
    return row

