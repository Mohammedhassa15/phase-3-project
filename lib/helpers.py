
from .db.bank import Bank
from .db.customer import Customer
from .db.account import Account
from .db.transaction import Transaction
from .db.base import Session

           # BANK SECTION
def create_bank(name, location):
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
	with Session() as session:
		try:
			banks = session.query(Bank).all()
			return [f"Bank(id={b.bank_id}, name='{b.bank_name}', location='{b.bank_location}')" for b in banks]
		except Exception as e:
			print(f"Error fetching banks: {e}")
			return []

def get_bank_by_id(bank_id):
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

             # CUSTOMER SECTION
def create_customer(name, email, bank_id):
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
	with Session() as session:
		try:
			customers = session.query(Customer).all()
			return [f"Customer(id={c.customer_id}, name='{c.name}', email='{c.email}', bank_id={c.bank_id})" for c in customers]
		except Exception as e:
			print(f"Error fetching customers: {e}")
			return []

def get_customer_by_id(customer_id):
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

               # ACCOUNT SECTION
def create_account(balance, customer_id):
	with Session() as session:
		try:
			new_account = Account(balance=balance, customer_id=customer_id)
			session.add(new_account)
			session.commit()
			return f"Account(id={new_account.account_id}, balance={new_account.balance}, customer_id={new_account.customer_id})"
		except Exception as e:
			session.rollback()
			print(f"Error creating account: {e}")
			return None

def get_all_accounts():
	with Session() as session:
		try:
			accounts = session.query(Account).all()
			return [f"Account(id={a.account_id}, balance={a.balance}, customer_id={a.customer_id})" for a in accounts]
		except Exception as e:
			print(f"Error fetching accounts: {e}")
			return []

def get_account_by_id(account_id):
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

           # TRANSACTION SECTION
def create_transaction(amount, account_id, transaction_type):
	from datetime import datetime
	with Session() as session:
		try:
			account = session.query(Account).filter_by(account_id=account_id).first()
			if not account:
				print(f"Account {account_id} not found.")
				return None
			if transaction_type == "withdrawal":
				# AVOID OVERDRAFT
				if account.balance is None or amount > account.balance:
					print(f"Error: Insufficient funds. Cannot withdraw {amount} from account {account_id} (balance: {account.balance})")
					return None
				account.balance -= amount
				print(f"[DEBUG] Account {account_id} balance after withdrawal: {account.balance}")
			elif transaction_type == "deposit":
				if account.balance is None:
					account.balance = 0
				account.balance += amount
				print(f"[DEBUG] Account {account_id} balance after deposit: {account.balance}")
			elif transaction_type == "transfer":
				if account.balance is None or amount > account.balance:
					print(f"Error: Insufficient funds. Cannot transfer {amount} from account {account_id} (balance: {account.balance})")
					return None
				account.balance -= amount
				print(f"[DEBUG] Account {account_id} balance after transfer: {account.balance}")
			else:
				print(f"Unknown transaction type: {transaction_type}")
				return None
			new_transaction = Transaction(amount=amount, account_id=account_id, transaction_type=transaction_type, transaction_date=datetime.now())
			session.add(new_transaction)
			session.commit()
			return f"Transaction(id={new_transaction.transaction_id}, amount={new_transaction.amount}, account_id={new_transaction.account_id}, type='{new_transaction.transaction_type}', date='{new_transaction.transaction_date}')"
		except Exception as e:
			session.rollback()
			print(f"Error creating transaction: {e}")
			return None
def get_all_transactions():
	with Session() as session:
		try:
			transactions = session.query(Transaction).all()
			return [f"Transaction(id={t.transaction_id}, amount={t.amount}, account_id={t.account_id}, type='{t.transaction_type}', date='{t.transaction_date}')" for t in transactions]
		except Exception as e:
			print(f"Error fetching transactions: {e}")
			return []

def get_transaction_by_id(transaction_id):
	with Session() as session:
		try:
			transaction = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
			if transaction:
				return f"Transaction(id={transaction.transaction_id}, amount={transaction.amount}, account_id={transaction.account_id}, type='{transaction.transaction_type}', date='{transaction.transaction_date}')"
			return None
		except Exception as e:
			print(f"Error fetching transaction by id: {e}")
			return None

def update_transaction(transaction_id, amount=None, account_id=None, transaction_type=None):
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
				return f"Transaction(id={transaction.transaction_id}, amount={transaction.amount}, account_id={transaction.account_id}, type='{transaction.transaction_type}', date='{transaction.transaction_date}')"
			return None
		except Exception as e:
			session.rollback()
			print(f"Error updating transaction: {e}")
			return None

def delete_transaction(transaction_id):
	with Session() as session:
		try:
			transaction = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
			if transaction:
				session.delete(transaction)
				session.commit()
				return f"Transaction(id={transaction.transaction_id}, amount={transaction.amount}, account_id={transaction.account_id}, type='{transaction.transaction_type}', date='{transaction.transaction_date}')"
			return None
		except Exception as e:
			session.rollback()
			print(f"Error deleting transaction: {e}")
			return None
