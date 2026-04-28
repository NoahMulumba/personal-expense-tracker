import csv
from datetime import date

FILE = "expenses.csv"

def calculate_total_expenses(filename):
    total = 0
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header row
            for row in reader:
                total += float(row[3])
    except FileNotFoundError:
        return 0
    return total

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total spending")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


import os

def add_expense():
    description = input("Description: ").strip()
    category = input("Category: ").strip()

    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number.")

    today = date.today().isoformat()
    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date", "description", "category", "amount"])
        writer.writerow([today, description, category, amount])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open(FILE, newline="") as file:
            reader = csv.reader(file)
            print("\nDate | Description | Category | Amount")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]} | R{row[3]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")


def total_expenses():
    total = calculate_total_expenses(FILE)
    if total == 0:
        print("No expenses recorded yet.")
    else:
        print(f"\nTotal spending: R{total:.2f}")



if __name__ == "__main__":
    main()
