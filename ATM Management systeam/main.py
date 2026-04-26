from balance import check_balance
from deposit import deposit
from withdraw import withdraw
from transaction import show_transactions
from pin import check_pin

balance = 1000
transactions = []

print("Welcome to ATM")

if not check_pin():
    print("Wrong PIN")
    exit()


def ATM_management(balance, transactions):   
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transactions")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance, transactions)

        elif choice == "3":
            balance = withdraw(balance, transactions)

        elif choice == "4":
            show_transactions(transactions)

        elif choice == "5":
            print("Thank you")
            break

        else:
            print("Invalid choice")

    return balance  



balance = ATM_management(balance, transactions)