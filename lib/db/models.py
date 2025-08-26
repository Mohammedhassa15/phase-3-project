from .base import Base, engine
from .bank import Bank
from .customer import Customer
from .account import Account
from .transaction import Transaction

#Dlete the table
Base.metadata.drop_all(engine)
# Create all tables
Base.metadata.create_all(engine)
print("All tables created successfully!")
