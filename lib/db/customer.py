from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base



class Customer(Base):
    __tablename__='customers'

    customer_id=Column(Integer(),primary_key =True)
    name =Column(String(),nullable =False)
    email=Column(String(),unique=True)
    bank_id =Column(Integer(),ForeignKey('banks.bank_id'))

    #customer belongs to a bank
    bank = relationship("Bank", back_populates="customers")
    #customer can have many accounts
    accounts = relationship("Account", back_populates='customer')

    def __repr__(self):
        return f"<Customer(customer_id={self.customer_id}, name={self.name}, email={self.email},bank_id={self.bank_id})>"
