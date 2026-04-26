from datetime import datetime

def withdraw(balance, transactions):
    amount = int(input("Enter amount: "))

    if amount > balance:
        print("Insufficient balance")
        transactions.append(str(datetime.now()) + " Failed Withdraw: " + str(amount))
    else:
        balance -= amount
        transactions.append(str(datetime.now()) + " Withdraw: " + str(amount))
        print("Withdraw successful")

    return balance