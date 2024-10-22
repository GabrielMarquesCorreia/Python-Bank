from account import BankAccount
from login import Login
from transference import made_transference
from deposit import made_deposit
from withdraw import made_withdraw
from extract import show_extract

gabriel = BankAccount('Gabriel', 1234, '1234', 1000)
arthur = BankAccount('Arthur', 12345, '12345', 1000)
eduardo = BankAccount('Eduardo', 123456, '123456', 1000)

accounts = [gabriel, arthur, eduardo]

# Menu

def account_menu(account):
    print(f"\nHello {account.name}! Welcome to the FakeBank!")
    while True:
        print("\n 1 - Balance   2 - Tranference   3 - Deposit   4 - Withdraw   5 - Extract   6 - LogOut   7 - Exit")
        op = input("\nChoose a option: ")

        if op == '1':
            print("\nBalance")
            print(f"Your actual balance is: R${account.balance}\n")
        elif op == '2':
            made_transference(account, accounts)
        elif op == '3':
            made_deposit(account)
        elif op == '4':
            made_withdraw(account)
        elif op == '5':
            show_extract(account)
        elif op == '6':
            print("\nLogged out....")
            return
        elif op == '7':
            print("\nExiting...")
            exit()
        else:
            print("\nPlease, select a valid option")
            return
        
# Login and menu simulation
while True: 
    print("\nFakeBank")
    account_number = int(input("Account number: "))
    passowrd = input("Password: ")
    login_account = Login(account_number, passowrd, accounts)

    if login_account:
        account_menu(login_account)
    else:
        print("Invalid account or password.")