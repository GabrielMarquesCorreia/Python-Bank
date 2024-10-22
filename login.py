from account import BankAccount

def Login(number_account, password, accounts):
    for account in accounts:
        if account.number == number_account and account.password == password:
            return account
    print("\nAccount not found!")
    return None