"""
Banking App Helper Functions
CRUD operations and business logic for Bank, Customer, Account, Transaction
"""

from .db.bank import Bank
from .db.account import Account
from .db.transaction import Transaction
from .db.customer import Customer
from .db.base import Session
from datetime import datetime

# BANK CRUD

def create_bank(name, location):
    """Create a new bank."""
    if not name or not location:
        print("Error: Bank name and location are required.")
        return None
    with Session() as session:
        try:
            new_bank = Bank(bank_name=name, bank_location=location)
            session.add(new_bank)
            session.commit()
            return f"Bank(id={new_bank.bank_id}, name='{new_bank.bank_name}', location='{new_bank.bank_location}')"
        except Exception as e:
            session.rollback()
            print(f"Error creating bank: {e}")
            return None

def get_all_banks():
    """List all banks."""
    with Session() as session:
        try:
            banks = session.query(Bank).all()
            return [f"Bank(id={b.bank_id}, name='{b.bank_name}', location='{b.bank_location}')" for b in banks]
        except Exception as e:
            print(f"Error fetching banks: {e}")
            return []

def get_bank_by_id(bank_id):
    """Get bank by id."""
    if bank_id is not None and int(bank_id) < 0:
        print(f"Error: Bank id cannot be negative. You entered: {bank_id}")
        return None
    with Session() as session:
        try:
            bank = session.query(Bank).filter_by(bank_id=bank_id).first()
            if bank:
                return f"Bank(id={bank.bank_id}, name='{bank.bank_name}', location='{bank.bank_location}')"
            return None
        except Exception as e:
            print(f"Error fetching bank by id: {e}")
            return None

def update_bank(bank_id, name=None, location=None):
    """Update bank details."""
    if bank_id is not None and int(bank_id) < 0:
        print(f"Error: Bank id cannot be negative. You entered: {bank_id}")
        return None
    with Session() as session:
        try:
            bank = session.query(Bank).filter_by(bank_id=bank_id).first()
            if bank:
                if name:
                    bank.bank_name = name
                if location:
                    bank.bank_location = location
                session.commit()
                return f"Bank(id={bank.bank_id}, name='{bank.bank_name}', location='{bank.bank_location}')"
            return None
        except Exception as e:
            session.rollback()
            print(f"Error updating bank: {e}")
            return None

def delete_bank(bank_id):
    """Delete a bank."""
    if bank_id is not None and int(bank_id) < 0:
        print(f"Error: Bank id cannot be negative. You entered: {bank_id}")
        return None
    with Session() as session:
        try:
            bank = session.query(Bank).filter_by(bank_id=bank_id).first()
            if bank:
                session.delete(bank)
                session.commit()
                return f"Bank(id={bank.bank_id}, name='{bank.bank_name}', location='{bank.bank_location}')"
            return None
        except Exception as e:
            session.rollback()
            print(f"Error deleting bank: {e}")
            return None

# CUSTOMER CRUD

def create_customer(name, email, bank_id):
    """Create a new customer."""
    if not name or not email:
        print("Error: Customer name and email are required.")
        return None
    if bank_id is not None and int(bank_id) < 0:
        print(f"Error: Bank id cannot be negative. You entered: {bank_id}")
        return None
    with Session() as session:
        try:
            new_customer = Customer(name=name, email=email, bank_id=bank_id)
            session.add(new_customer)
            session.commit()
            return f"Customer(id={new_customer.customer_id}, name='{new_customer.name}', email='{new_customer.email}', bank_id={new_customer.bank_id})"
        except Exception as e:
            session.rollback()
            print(f"Error creating customer: {e}")
            return None

def get_all_customers():
    """List all customers."""
    with Session() as session:
        try:
            customers = session.query(Customer).all()
            return [f"Customer(id={c.customer_id}, name='{c.name}', email='{c.email}', bank_id={c.bank_id})" for c in customers]
        except Exception as e:
            print(f"Error fetching customers: {e}")
            return []

def get_customer_by_id(customer_id):
    """Get customer by id."""
    if customer_id is not None and int(customer_id) < 0:
        print(f"Error: Customer id cannot be negative. You entered: {customer_id}")
        return None
    with Session() as session:
        try:
            customer = session.query(Customer).filter_by(customer_id=customer_id).first()
            if customer:
                return f"Customer(id={customer.customer_id}, name='{customer.name}', email='{customer.email}', bank_id={customer.bank_id})"
            return None
        except Exception as e:
            print(f"Error fetching customer by id: {e}")
            return None

def update_customer(customer_id, name=None, email=None, bank_id=None):
    """Update customer details."""
    if customer_id is not None and int(customer_id) < 0:
        print(f"Error: Customer id cannot be negative. You entered: {customer_id}")
        return None
    if bank_id is not None and int(bank_id) < 0:
        print(f"Error: Bank id cannot be negative. You entered: {bank_id}")
        return None
    with Session() as session:
        try:
            customer = session.query(Customer).filter_by(customer_id=customer_id).first()
            if customer:
                if name:
                    customer.name = name
                if email:
                    customer.email = email
                if bank_id:
                    customer.bank_id = bank_id
                session.commit()
                return f"Customer(id={customer.customer_id}, name='{customer.name}', email='{customer.email}', bank_id={customer.bank_id})"
            return None
        except Exception as e:
            session.rollback()
            print(f"Error updating customer: {e}")
            return None

def delete_customer(customer_id):
    """Delete a customer."""
    if customer_id is not None and int(customer_id) < 0:
        print(f"Error: Customer id cannot be negative. You entered: {customer_id}")
        return None
    with Session() as session:
        try:
            customer = session.query(Customer).filter_by(customer_id=customer_id).first()
            if customer:
                session.delete(customer)
                session.commit()
                return f"Customer(id={customer.customer_id}, name='{customer.name}', email='{customer.email}', bank_id={customer.bank_id})"
            return None
        except Exception as e:
            session.rollback()
            print(f"Error deleting customer: {e}")
            return None

# ACCOUNT CRUD

def create_account(balance, customer_id):
    """Create a new account."""
    if customer_id is not None and int(customer_id) < 0:
        print(f"Error: Customer id cannot be negative. You entered: {customer_id}")
        return None
    try:
        bal = float(balance)
    except Exception as e:
        print(f"Error: Invalid balance type. {e}")
        return None
    if bal < 0:
        print(f"Error: Initial balance cannot be negative. You entered: {bal}")
        return None
    with Session() as session:
        try:
            new_account = Account(balance=bal, customer_id=customer_id)
            session.add(new_account)
            session.commit()
            return f"Account(id={new_account.account_id}, balance={new_account.balance}, customer_id={new_account.customer_id})"
        except Exception as e:
            session.rollback()
            print(f"Error creating account: {e}")
            return None

def get_all_accounts():
    """List all accounts."""
    with Session() as session:
        try:
            accounts = session.query(Account).all()
            return [f"Account(id={a.account_id}, balance={a.balance}, customer_id={a.customer_id})" for a in accounts]
        except Exception as e:
            print(f"Error fetching accounts: {e}")
            return []

def get_account_by_id(account_id):
    """Get account by id."""
    if account_id is not None and int(account_id) < 0:
        print(f"Error: Account id cannot be negative. You entered: {account_id}")
        return None
    with Session() as session:
        try:
            account = session.query(Account).filter_by(account_id=account_id).first()
            if account:
                return f"Account(id={account.account_id}, balance={account.balance}, customer_id={account.customer_id})"
            return None
        except Exception as e:
            print(f"Error fetching account by id: {e}")
            return None

def update_account(account_id, balance=None, customer_id=None):
    """Update account details."""
    if account_id is not None and int(account_id) < 0:
        print(f"Error: Account id cannot be negative. You entered: {account_id}")
        return None
    if balance is not None and float(balance) < 0:
        print(f"Error: Balance cannot be negative. You entered: {balance}")
        return None
    if customer_id is not None and int(customer_id) < 0:
        print(f"Error: Customer id cannot be negative. You entered: {customer_id}")
        return None
    with Session() as session:
        try:
            account = session.query(Account).filter_by(account_id=account_id).first()
            if account:
                if balance is not None:
                    account.balance = balance
                if customer_id:
                    account.customer_id = customer_id
                session.commit()
                return f"Account(id={account.account_id}, balance={account.balance}, customer_id={account.customer_id})"
            return None
        except Exception as e:
            session.rollback()
            print(f"Error updating account: {e}")
            return None

def delete_account(account_id):
    """Delete an account."""
    if account_id is not None and int(account_id) < 0:
        print(f"Error: Account id cannot be negative. You entered: {account_id}")
        return None
    with Session() as session:
        try:
            account = session.query(Account).filter_by(account_id=account_id).first()
            if account:
                session.delete(account)
                session.commit()
                return f"Account(id={account.account_id}, balance={account.balance}, customer_id={account.customer_id})"
            return None
        except Exception as e:
            session.rollback()
            print(f"Error deleting account: {e}")
            return None

# TRANSACTION CRUD & LOGIC

def create_transaction(amount, account_id, transaction_type):
    """Create a transaction with business logic and validation."""
    try:
        amt = float(amount)
        acc_id = int(account_id)
    except Exception as e:
        print(f"Error: Invalid input type for amount or account_id. {e}")
        return None
    if amt < 0:
        print(f"Error: Negative amounts are not allowed for transactions. You entered: {amt}")
        return None
    if acc_id < 0:
        print(f"Error: Account id cannot be negative. You entered: {acc_id}")
        return None
    with Session() as session:
        try:
            account = session.query(Account).filter_by(account_id=acc_id).first()
            if not account:
                print(f"Account {acc_id} not found.")
                return None
            if transaction_type == "withdrawal":
                if account.balance is None or amt > account.balance:
                    print(f"Error: Insufficient funds. Cannot withdraw {amt} from account {acc_id} (balance: {account.balance})")
                    return None
                account.balance -= amt
            elif transaction_type == "deposit":
                if account.balance is None:
                    account.balance = 0
                account.balance += amt
            elif transaction_type == "transfer":
                if account.balance is None or amt > account.balance:
                    print(f"Error: Insufficient funds. Cannot transfer {amt} from account {acc_id} (balance: {account.balance})")
                    return None
                account.balance -= amt
            else:
                print(f"Unknown transaction type: {transaction_type}")
                return None
            new_transaction = Transaction(amount=amt, account_id=acc_id, transaction_type=transaction_type, transaction_date=datetime.now())
            session.add(new_transaction)
            session.commit()
            formatted_date = new_transaction.transaction_date.strftime('%Y-%m-%d %H:%M:%S')
            return f"Transaction(id={new_transaction.transaction_id}, amount={new_transaction.amount}, account_id={new_transaction.account_id}, type='{new_transaction.transaction_type}', date='{formatted_date}')"
        except Exception as e:
            session.rollback()
            print(f"Error creating transaction: {e}")
            return None

def get_all_transactions():
    """List all transactions."""
    with Session() as session:
        try:
            transactions = session.query(Transaction).all()
            return [f"Transaction(id={t.transaction_id}, amount={t.amount}, account_id={t.account_id}, type='{t.transaction_type}', date='{t.transaction_date.strftime('%Y-%m-%d %H:%M:%S')}')" for t in transactions]
        except Exception as e:
            print(f"Error fetching transactions: {e}")
            return []

def get_transaction_by_id(transaction_id):
    """Get transaction by id."""
    with Session() as session:
        try:
            transaction = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
            if transaction:
                formatted_date = transaction.transaction_date.strftime('%Y-%m-%d %H:%M:%S')
                return f"Transaction(id={transaction.transaction_id}, amount={transaction.amount}, account_id={transaction.account_id}, type='{transaction.transaction_type}', date='{formatted_date}')"
            return None
        except Exception as e:
            print(f"Error fetching transaction by id: {e}")
            return None

def update_transaction(transaction_id, amount=None, account_id=None, transaction_type=None):
    """Update transaction details."""
    with Session() as session:
        try:
            transaction = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
            if transaction:
                if amount is not None:
                    transaction.amount = amount
                if account_id:
                    transaction.account_id = account_id
                if transaction_type:
                    transaction.transaction_type = transaction_type
                session.commit()
                formatted_date = transaction.transaction_date.strftime('%Y-%m-%d %H:%M:%S')
                return f"Transaction(id={transaction.transaction_id}, amount={transaction.amount}, account_id={transaction.account_id}, type='{transaction.transaction_type}', date='{formatted_date}')"
            return None
        except Exception as e:
            session.rollback()
            print(f"Error updating transaction: {e}")
            return None

def delete_transaction(transaction_id):
    """Delete a transaction."""
    with Session() as session:
        try:
            transaction = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
            if transaction:
                session.delete(transaction)
                session.commit()
                formatted_date = transaction.transaction_date.strftime('%Y-%m-%d %H:%M:%S')
                return f"Transaction(id={transaction.transaction_id}, amount={transaction.amount}, account_id={transaction.account_id}, type='{transaction.transaction_type}', date='{formatted_date}')"
            return None
        except Exception as e:
            session.rollback()
            print(f"Error deleting transaction: {e}")
            return None
