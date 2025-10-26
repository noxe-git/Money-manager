import flet as ft
import sqlite3 as sql
from sqlsettings import DatabaseSettings

db = DatabaseSettings()

db.create_table()


def main(page: ft.Page):
    
    page.title = "Money Manager"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    '''Constants and UI elements'''
    
    transactions_list = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True, height=300)

    #text fields
    How_much_money = ft.TextField(label='How much money?', width=300, on_change=lambda e: validate_input(e))
    Category = ft.TextField(label='Category of expense/income', width=300, on_change=lambda e: validate_input(e))

    #buttons
    submit_button = ft.ElevatedButton(text="Submit", width=150, disabled=True, on_click=lambda e: submit_transaction(e))
    Theme_button = ft.IconButton(icon=ft.Icons.DARK_MODE, on_click=lambda e: change_theme(e))
    Clear_button = ft.ElevatedButton(text="clear", width=150, on_click=lambda e: reset_fields(e))
    Check_button = ft.ElevatedButton(text="Check all transactions", width=150, on_click=lambda e: check_transactions(e))

    #dropdowns
    dd2 = ft.Dropdown(label="select income or expense",
                      options=[
                          ft.dropdown.Option("Income"),
                          ft.dropdown.Option("Expense"),
                      ],)

    dd = ft.Dropdown(label="Select a currency type",
        width=200,
        options=[
            ft.dropdown.Option("$"),
            ft.dropdown.Option("€"),
            ft.dropdown.Option("£"),
            ft.dropdown.Option("₴"),
            ft.dropdown.Option("₽"),
        ],)

    

# function to change theme
    def change_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    def validate_input(e):
        if How_much_money.value:
            submit_button.disabled = False
        else:
            submit_button.disabled = True
        page.update()


# function to submit a transaction
    def submit_transaction(e):
        if not How_much_money.value or not dd.value or not dd2.value:
            return
        amount = float(How_much_money.value)
        if dd2.value == "Income":
            t_type = "Income"
        else:
            t_type = "Expense"
        db.add_transaction(amount, Category.value, t_type)
        How_much_money.value = ""
        Category.value = ""
        dd2.value = None
        dd.value = None
        submit_button.disabled = True
        page.update()

# function to reset input fields
    def reset_fields(e):
       page.controls.clear()
       How_much_money.value = ""
       Category.value = ""
       dd2.value = None
       dd.value = None
       submit_button.disabled = True
       transactions_list.controls.clear()
       add_layout()
       page.update()


# function to check and display all transactions
    def check_transactions(e):
        transactions = db.get_transactions()
        if not transactions:
            page.add(ft.Text("No transactions found."))
            page.update()
            return
        # create a ListView for displaying transactions
        
        for tx in transactions:
            transactions_list.controls.append(ft.Text(f"ID: {tx['id']}, Amount: {tx['amount']}, "
                f"Category: {tx['category']}, Type: {tx['type']}, "
                f"Date: {tx['created_at']}"))
        page.add(transactions_list)
        page.update()


# Layout

    def add_layout():
        page.add(ft.Row(
            [ft.Text("Program to manage your money:)",
                    size=30, weight=ft.FontWeight.BOLD),
            Theme_button], alignment=ft.MainAxisAlignment.CENTER
            ),ft.Row(
            [dd, dd2
            ], alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [How_much_money],
                alignment=ft.MainAxisAlignment.CENTER)
                        )


        page.add(ft.Row([submit_button], alignment=ft.MainAxisAlignment.CENTER), Clear_button, Check_button)
        page.update()

    add_layout()




# Run the app
if __name__ == "__main__":
    ft.app(target=main)

# Close the database connection when the app is closed
db.close()