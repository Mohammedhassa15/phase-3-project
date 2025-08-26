from .helpers import (
    create_bank, 
    get_all_banks, 
    get_bank_by_id, 
    update_bank, 
    delete_bank,
    create_customer,
    get_all_customers,
    get_customer_by_id, 
    update_customer,
    delete_customer,
    create_account,
    get_all_accounts,
    get_account_by_id,
    update_account, 
    delete_account,
    create_transaction,
    get_all_transactions,
    get_transaction_by_id,
    update_transaction,
    delete_transaction
)

def exit_program():
    print("Exiting program.")
    exit()

def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. List all banks")
    print("2. Find bank by id")
    print("3. Create bank")
    print("4. Update bank")
    print("5. Delete bank")
    print("6. List all customers")
    print("7. Find customer by id")
    print("8. Create customer")
    print("9. Update customer")
    print("10. Delete customer")
    print("11. List all accounts")
    print("12. Find account by id")
    print("13. Create account")
    print("14. Update account")
    print("15. Delete account")
    print("16. List all transactions")
    print("17. Find transaction by id")
    print("18. Create transaction")
    print("19. Update transaction")
    print("20. Delete transaction")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            banks = get_all_banks()
            for bank in banks:
                print(bank)
        elif choice == "2":
            while True:
                bank_id_input = input("Enter bank id: ")
                try:
                    bank_id = int(bank_id_input)
                    if bank_id < 0:
                        print("Bank id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid bank id. Please enter a positive integer.")
            print(get_bank_by_id(bank_id))
        elif choice == "3":
            name = input("Bank name: ")
            location = input("Bank location: ")
            print(create_bank(name, location))
        elif choice == "4":
            while True:
                bank_id_input = input("Bank id: ")
                try:
                    bank_id = int(bank_id_input)
                    if bank_id < 0:
                        print("Bank id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid bank id. Please enter a positive integer.")
            name = input("New name (leave blank to skip): ")
            location = input("New location (leave blank to skip): ")
            print(update_bank(bank_id, name or None, location or None))
        elif choice == "5":
            while True:
                bank_id_input = input("Bank id: ")
                try:
                    bank_id = int(bank_id_input)
                    if bank_id < 0:
                        print("Bank id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid bank id. Please enter a positive integer.")
            print(delete_bank(bank_id))
        elif choice == "6":
            customers = get_all_customers()
            for customer in customers:
                print(customer)
        elif choice == "7":
            while True:
                customer_id_input = input("Customer id: ")
                try:
                    customer_id = int(customer_id_input)
                    if customer_id < 0:
                        print("Customer id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid customer id. Please enter a positive integer.")
            print(get_customer_by_id(customer_id))
        elif choice == "8":
            name = input("Customer name: ")
            email = input("Customer email: ")
            bank_id = input("Bank id: ")
            print(create_customer(name, email, bank_id))
        elif choice == "9":
            while True:
                customer_id_input = input("Customer id: ")
                try:
                    customer_id = int(customer_id_input)
                    if customer_id < 0:
                        print("Customer id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid customer id. Please enter a positive integer.")
            name = input("New name (leave blank to skip): ")
            email = input("New email (leave blank to skip): ")
            bank_id = input("New bank id (leave blank to skip): ")
            bank_id = int(bank_id) if bank_id else None
            print(update_customer(customer_id, name or None, email or None, bank_id))
        elif choice == "10":
            while True:
                customer_id_input = input("Customer id: ")
                try:
                    customer_id = int(customer_id_input)
                    if customer_id < 0:
                        print("Customer id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid customer id. Please enter a positive integer.")
            print(delete_customer(customer_id))
        elif choice == "11":
            accounts = get_all_accounts()
            for account in accounts:
                print(account)
        elif choice == "12":
            while True:
                account_id_input = input("Account id: ")
                try:
                    account_id = int(account_id_input)
                    if account_id < 0:
                        print("Account id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid account id. Please enter a positive integer.")
            print(get_account_by_id(account_id))
        elif choice == "13":
            while True:
                balance_input = input("Initial balance: ")
                try:
                    balance = float(balance_input)
                    if balance < 0:
                        print("Initial balance cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid balance. Please enter a positive number.")
            customer_id = input("Customer id: ")
            print(create_account(balance, customer_id))
        elif choice == "14":
            while True:
                account_id_input = input("Account id: ")
                try:
                    account_id = int(account_id_input)
                    if account_id < 0:
                        print("Account id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid account id. Please enter a positive integer.")
            balance = input("New balance (leave blank to skip): ")
            customer_id = input("New customer id (leave blank to skip): ")
            customer_id = int(customer_id) if customer_id else None
            print(update_account(account_id, float(balance) if balance else None, customer_id))
        elif choice == "15":
            while True:
                account_id_input = input("Account id: ")
                try:
                    account_id = int(account_id_input)
                    if account_id < 0:
                        print("Account id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid account id. Please enter a positive integer.")
            print(delete_account(account_id))
        elif choice == "16":
            transactions = get_all_transactions()
            for transaction in transactions:
                print(transaction)
        elif choice == "17":
            while True:
                transaction_id_input = input("Transaction id: ")
                try:
                    transaction_id = int(transaction_id_input)
                    if transaction_id < 0:
                        print("Transaction id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid transaction id. Please enter a positive integer.")
            print(get_transaction_by_id(transaction_id))
        elif choice == "18":
            while True:
                amount_input = input("Amount: ")
                try:
                    amount = float(amount_input)
                    if amount < 0:
                        print("Amount cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            account_id = input("Account id: ")
            transaction_type = input("Type (deposit/transfer/withdrawal): ")
            print(create_transaction(amount, account_id, transaction_type))
        elif choice == "19":
            while True:
                transaction_id_input = input("Transaction id: ")
                try:
                    transaction_id = int(transaction_id_input)
                    if transaction_id < 0:
                        print("Transaction id cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid transaction id. Please enter a positive integer.")
            while True:
                amount_input = input("New amount (leave blank to skip): ")
                if not amount_input:
                    amount = None
                    break
                try:
                    amount = float(amount_input)
                    if amount < 0:
                        print("Amount cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            account_id = input("New account id (leave blank to skip): ")
            transaction_type = input("New type (leave blank to skip): ")
            account_id = int(account_id) if account_id else None
            print(update_transaction(transaction_id, float(amount) if amount else None, account_id, transaction_type or None))
        elif choice == "20":
            transaction_id = int(input("Transaction id: "))
            print(delete_transaction(transaction_id))
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
