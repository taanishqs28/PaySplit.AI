"""
Database models for PaySplit.AI transactions.

This module defines the database schema for:
- Transaction records
- User accounts (future feature)
- Categories (future feature)
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.sql import func
from app.core.database import Base


class Transaction(Base):
    """
    Transaction model for storing financial transaction data.
    
    This model represents individual transactions uploaded by users,
    with fields for amount, description, date, and categorization.
    """
    
    __tablename__ = "transactions"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Transaction details
    date = Column(DateTime, nullable=False, index=True)
    description = Column(Text, nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String(50), nullable=False)  # 'Income' or 'Expense'
    
    # Categorization fields (for future AI features)
    category = Column(String(100), nullable=True)
    is_business = Column(Boolean, default=False)
    business_percentage = Column(Float, default=0.0)  # 0.0 to 1.0
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # User association (for future multi-user support)
    user_id = Column(Integer, nullable=True, index=True)
    
    def __repr__(self):
        """String representation of the transaction."""
        return f"<Transaction(id={self.id}, description='{self.description}', amount={self.amount})>"
    
    def to_dict(self):
        """Convert transaction to dictionary for API responses."""

        date = getattr(self, 'date', None)
        created_at = getattr(self, 'created_at', None)
        updated_at = getattr(self, 'updated_at', None)

        return {
            "id": self.id,
            "date": self.date.isoformat() if date else None,
            "description": self.description,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "category": self.category,
            "is_business": self.is_business,
            "business_percentage": self.business_percentage,
            "created_at": self.created_at.isoformat() if created_at else None,
            "updated_at": self.updated_at.isoformat() if updated_at else None,
        } 