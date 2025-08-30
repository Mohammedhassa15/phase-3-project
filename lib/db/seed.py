
from .base import Session
from .bank import Bank
from .customer import Customer
from .account import Account
from .transaction import Transaction

session = Session()

# --- Add Banks ---
bank1 = Bank(bank_name="Equity Bank", bank_location="Nairobi")
bank2 = Bank(bank_name="KCB Bank", bank_location="Mombasa")
session.add_all([bank1, bank2])
session.commit()

# --- Add Customers ---
customer1 = Customer(name="Mohammed", email="mohammed0041@gmail.com", bank=bank1)
customer2 = Customer(name="Hassan", email="hassan0879@gmail.com", bank=bank2)
session.add_all([customer1, customer2])
session.commit()

# --- Add Accounts ---
account1 = Account(balance=12000, customer=customer1)
account2 = Account(balance=15000, customer=customer2)
session.add_all([account1, account2])
session.commit()

# --- Add Transactions ---
transaction1 = Transaction(amount=5000, account=account1, transaction_type="deposit")
transaction2 = Transaction(amount=2000, account=account2, transaction_type="withdrawal")
session.add_all([transaction1, transaction2])
session.commit()

print("Info seeded successfully!")
