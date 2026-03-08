import sys
from datetime import datetime
from tracker import service

def get_valid_type():
    while True:
        t_type = input("Enter transaction type (income/expense): ").strip().lower()
        if t_type in ["income", "expense"]:
            return t_type
        print("Invalid type! Please enter 'income' or 'expense'.")

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            if amount > 0:
                return amount
            print("Amount must be a positive number.")
        except ValueError:
            print("Invalid amount! Please enter a number.")

def get_valid_date():
    while True:
        date_str = input("Enter month (YYYY-MM, e.g., 2026-03): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m")
            return date_str
        except ValueError:
            print("Invalid format! Please enter the month in YYYY-MM format.")

def main():
    print("Welcome to Income-Expense Tracker!")
    while True:
        print("\nMain Menu:")
        print("1. Create a transaction")
        print("2. Get all transactions of a given month")
        print("3. Get monthly summary of a given month")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            t_type = get_valid_type()
            amount = get_valid_amount()
            description = input("Enter description: ").strip()
            
            transaction = service.create_transaction(t_type, amount, description)
            print(f"\nTransaction created successfully!")
            print(f"ID: {transaction.id}, Type: {transaction.type}, Amount: {transaction.amount}, Date: {transaction.date}, Description: {transaction.description}")

        elif choice == "2":
            date = get_valid_date()
            transactions = service.get_transactions(date)

            if not transactions:
                print(f"\nNo transactions found for {date}.")
            else:
                print(f"\nTransactions for {date}:")
                print(f"{'ID':<18} | {'Type':<8} | {'Amount':<10} | {'Date':<10} | {'Description'}")
                print("-" * 80)
                for t in transactions:
                    print(f"{t.id:<18} | {t.type:<8} | {t.amount:<10.2f} | {t.date:<10} | {t.description}")

        elif choice == "3":
            date = get_valid_date()
            transactions = service.get_transactions(date)
            
            if not transactions:
                print(f"\nNo data available for {date} to generate a summary.")
            else:
                total_income, total_expense, balance = service.get_monthly_summary(transactions)
                print(f"\nMonthly Summary for {date}:")
                print("-" * 30)
                print(f"Total Income:  {total_income:>10.2f}")
                print(f"Total Expense: {total_expense:>10.2f}")
                print(f"Balance:       {balance:>10.2f}")
                print("-" * 30)

        elif choice == "4":
            print("Exiting tracker. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
