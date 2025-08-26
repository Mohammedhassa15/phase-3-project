from sqlalchemy import Column, Integer,  ForeignKey, Float, DateTime, func, Enum
from sqlalchemy.orm import relationship
from .base import Base 


class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.account_id'))
    transaction_date = Column(DateTime, default=func.now())
    transaction_type = Column(
        Enum('deposit', 'transfer', 'withdrawal', name='transaction_type'),
        nullable=False,
        default='deposit'
    )


    account = relationship("Account", back_populates="transactions")

    def __repr__(self):
        return (
            f"<Transaction(transaction_id={self.transaction_id}, "
            f"account_id={self.account_id}, "
            f"transaction_date={self.transaction_date}, "
            f"transaction_type={self.transaction_type}, "
            f"amount={self.amount})>"
        )
