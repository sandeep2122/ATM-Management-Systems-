def show_transactions(transactions):
    if len(transactions) == 0:
        print("No transactions")
    else:
        print("\n--- Transactions ---")
        for t in transactions:
            print(t)