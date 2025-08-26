from sqlalchemy import Column,Integer,String 
from sqlalchemy.orm import relationship
from .base import Base






class Bank(Base):
    __tablename__ = 'banks'

    bank_id = Column(Integer(), primary_key = True)
    bank_name = Column(String, nullable = False)
    bank_location= Column(String)
    # one bank can have many accounts
    customers = relationship("Customer", back_populates="bank")

    def __repr__(self):
        return f"Bank(id={self.bank_id}, name='{self.bank_name}', location='{self.bank_location}')"
    