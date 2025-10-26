# Money Manager

Money Manager is a simple GUI application for tracking personal finances. It allows users to record income and expenses, categorize transactions, and view transaction history using a SQLite database.

## Features
- **Add Transactions**: Record income or expenses with amount, currency, category, and type.
- **View Transactions**: Display a list of all recorded transactions with details (ID, amount, category, type, date).
- **Theme Switching**: Toggle between dark and light themes with a single click (default: dark theme).
- **SQLite Integration**: Store transactions persistently in a lightweight SQLite database.
- **User-Friendly Interface**: Built with Flet for a clean and intuitive experience.

## Prerequisites
- **Python**: Version 3.8 or higher.
- **Flet**: Python library for creating GUI (`pip install flet`).
- **SQLite**: Included in Python's standard library (`sqlite3`).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/money-manager.git
2. **Install depencies**
  cd money-manager
  Install Dependencies:
  Ensure Python is installed, then install Flet:
  pip install flet   
  python3 main.py

## Usage
1.**Launch app**
Run: main.py
2.**add a Transaction:**
-Enter the amount in the "How much money?" field.
-Select a currency from the dropdown (e.g., $, €, £, ₴, ₽).
-Choose the transaction type (Income or Expense).
-Optionally, specify a category (e.g., "Food", "Salary").
-Click "Submit" to save the transaction.
3. **Viev a transactions**

##Project Structure
-main.py: Contains the GUI logic and application entry point.
-sqlsettings.py: Manages SQLite database operations (create table, add/get transactions).
-README.md: This file, providing project documentation.

##Future Improvements
-Add editing and deletion of transactions.
-Implement transaction filtering by date, category, or type.
-Display summary statistics (e.g., total balance, category breakdowns).
-Add input validation for better error handling.

##Contact
For questions or feedback, please open an issue.
Thank you for using Money Manager:3!
