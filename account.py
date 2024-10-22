class BankAccount:
    def __init__(self, account_name, account_number, password, balance=0):
        self.name = account_name
        self.number = account_number
        self.password = password
        self.balance = balance
        self.extract = []

    def deposit(self, amount):
        self.balance += amount
        self.extract.append(f"Deposit: R${amount}")
        print(f"Deposit of R${amount} to your account was successful.")

    def withdraw(self, amount):
        self.balance -= amount
        self.extract.append(f"Withdrawal: R${amount}")
        print(f"Withdrawal of R${amount} from your account was successful.")

    def transferencia(self, amount, destination_account):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            destination_account.balance += amount
            self.extract.append(f"Transfer: R${amount} to {destination_account.name} (Account: {destination_account.number})")
            destination_account.extract.append(f"Transfer: R${amount} from {self.name} (Account: {self.number})")
            print(f"Transfer of R${amount} to {destination_account.name} (Account: {destination_account.number}) was successful!")
