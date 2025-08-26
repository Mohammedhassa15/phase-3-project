from  sqlalchemy import Column,Integer,String,ForeignKey,Float
from sqlalchemy.orm import relationship
from .base import Base


class Account(Base):
    __tablename__= 'accounts'
    account_id = Column(Integer(), primary_key = True,autoincrement=True)
    balance = Column(Float(),default=0)
    customer_id = Column(Integer(),ForeignKey('customers.customer_id'))

    customer =relationship("Customer", back_populates='accounts')
    transactions=relationship("Transaction", back_populates='account')

    def __repr__(self):
        return f"<Account {self.account_id}: {self.customer.name}, balance={self.balance}>"


