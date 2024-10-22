def made_deposit(account):
    print("\nDeposit")
    amount = float(input("Deposit amount: "))
    account.deposit(amount)
