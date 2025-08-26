from .base import Session
from bank import Bank
from customer import Customer
from account import Account
from transaction import Transaction

session = Session()

# Get all banks and their related data
banks = session.query(Bank).all()

for bank in banks:
    print(f"Bank: {bank.bank_name}, Location: {bank.bank_location}")
    
    for customer in bank.customers:
        print(f"  Customer: {customer.name}, Email: {customer.email}")
        
        for account in customer.accounts:
            print(f"    Account ID: {account.account_id}, Balance: {account.balance}")
            
            