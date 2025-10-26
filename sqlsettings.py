import sqlite3 as sql


# Database class settings
class DatabaseSettings:
    """Small wrapper around sqlite3 connection for transactions table.

    Contract:
      - inputs: db_name (str)
      - outputs: methods to add/get/close DB
      - errors: sqlite3 exceptions may be raised to caller
    """

    # Initialize the database connection and create the transactions table
    def __init__(self, db_name='money_manager.db'):
        # allow usage from GUI thread(s) if needed
        self.database = sql.connect(db_name, check_same_thread=False)
        # return sqlite3.Row objects so callers can access columns by name
        self.database.row_factory = sql.Row
        self.cursor = self.database.cursor()
        self.create_table()

    # Create the transactions table
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                type TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        # Commit the changes
        self.database.commit()

    # Add a new transaction using parameterized query
    def add_transaction(self, amount, category, t_type):
        """Insert a transaction. Use parameterized query to avoid injection.

        amount: float
        category: str
        t_type: str (e.g. 'Income' or 'Expense')
        """
        self.cursor.execute(
            'INSERT INTO transactions (amount, category, type) VALUES (?, ?, ?)',
            (amount, category, t_type),
        )
        self.database.commit()

    # Retrieve all transactions
    def get_transactions(self):
        self.cursor.execute('SELECT * FROM transactions')
        rows = self.cursor.fetchall()
        return rows

    # Close the database connection
    def close(self):
        self.database.close()

