from datetime import datetime

def deposit(balance, transactions):
    try:
        amount = int(input("Enter amount: "))
        balance += amount
        transactions.append(f"{datetime.now()} | Deposited: {amount}")
        print("Deposited successfully")
    except:
        print("Invalid input")
    return balance