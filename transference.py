def made_transference(account_origin, accounts):
    print("\nTransference")
    account_destination_number = int(input("Account number: "))
    amount = int(input("Amount: "))
    account_destination = next((c for c in accounts if c.number == account_destination_number), None) 

    if account_destination: 
        account_origin.transferencia(amount, account_destination)
    else:
        print("\nAccount not found.")
        return
