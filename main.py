from datetime import datetime

expenses = []


def add_expense():
    name = input("Enter name: ")
    amount = float(input("Enter amount paid: "))
    category = input("Enter category (Food/Travel/Snacks/Rent/Other): ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    expenses.append(expense)


def calculate_report():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    share = total / len(expenses)

    return total, share


def show_report():
    total, share = calculate_report()

    print("\nExpense History:")
    for expense in expenses:
        print(expense["name"], "-", expense["category"], "- ₹", expense["amount"], "-", expense["date"])

    print("\nTotal Expense:", total)
    print("Each Person Share:", share)

    print("\nFinal Balance:")
    for expense in expenses:
        balance = expense["amount"] - share

        if balance > 0:
            print(expense["name"], "should receive ₹", round(balance, 2))
        elif balance < 0:
            print(expense["name"], "should pay ₹", round(abs(balance), 2))
        else:
            print(expense["name"], "is settled")


def save_report():
    total, share = calculate_report()

    with open("expenses.txt", "w", encoding="utf-8") as file:
        file.write("Hostel Expense Splitter Report\n")
        file.write("--------------------------------\n\n")

        file.write("Expense History:\n")
        for expense in expenses:
            file.write(
                f"{expense['name']} - {expense['category']} - ₹{expense['amount']} - {expense['date']}\n"
            )

        file.write(f"\nTotal Expense: ₹{total}\n")
        file.write(f"Each Person Share: ₹{share}\n\n")

        file.write("Final Balance:\n")
        for expense in expenses:
            balance = expense["amount"] - share

            if balance > 0:
                result = f"{expense['name']} should receive ₹{round(balance, 2)}"
            elif balance < 0:
                result = f"{expense['name']} should pay ₹{round(abs(balance), 2)}"
            else:
                result = f"{expense['name']} is settled"

            file.write(result + "\n")

    print("\nReport saved successfully in expenses.txt")


while True:
    print("\n===== Hostel Expense Splitter =====")
    print("1. Add Expense")
    print("2. Show Report")
    print("3. Save Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            show_report()
    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses to save.")
        else:
            save_report()
    elif choice == "4":
        print("Thank you for using Hostel Expense Splitter!")
        break
    else:
        print("Invalid choice. Please try again.")