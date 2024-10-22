def made_withdraw(account):
    print("\nWithdraw")
    amount = float(input("Withdraw amount: "))
    account.withdraw(amount)