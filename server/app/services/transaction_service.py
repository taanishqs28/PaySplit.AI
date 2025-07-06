"""
Transaction service for database operations.

This module handles all database interactions for transactions:
- Creating new transactions
- Retrieving transactions
- Updating transaction data
- Deleting transactions
"""

from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional, Dict, Any
from app.models.transaction import Transaction


class TransactionService:
    """Service class for transaction database operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def create_transaction(self, transaction_data: Dict[str, Any]) -> Transaction:
        """
        Create a new transaction in the database.
        
        Args:
            transaction_data: Dictionary containing transaction information
            
        Returns:
            Transaction: The created transaction object
        """
        # Parse date string to datetime object
        if isinstance(transaction_data.get('Date'), str):
            try:
                date = datetime.strptime(transaction_data['Date'], '%Y-%m-%d')
            except ValueError:
                # Fallback to current date if parsing fails
                date = datetime.now()
        else:
            date = datetime.now()
        
        # Create transaction object
        transaction = Transaction(
            date=date,
            description=transaction_data.get('Description', ''),
            amount=float(transaction_data.get('Amount', 0.0)),
            transaction_type=transaction_data.get('Type', 'Expense'),
            category=None,  # Will be set by AI categorization later
            is_business=False,  # Will be determined by AI later
            business_percentage=0.0  # Will be calculated later
        )
        
        # Save to database
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        
        return transaction
    
    def get_all_transactions(self, limit: int = 100) -> List[Transaction]:
        """
        Retrieve all transactions from the database.
        
        Args:
            limit: Maximum number of transactions to return
            
        Returns:
            List[Transaction]: List of transaction objects
        """
        return self.db.query(Transaction).limit(limit).all()
    
    def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]:
        """
        Retrieve a specific transaction by ID.
        
        Args:
            transaction_id: The ID of the transaction to retrieve
            
        Returns:
            Optional[Transaction]: The transaction object or None if not found
        """
        return self.db.query(Transaction).filter(Transaction.id == transaction_id).first()
    
    def get_transactions_by_type(self, transaction_type: str) -> List[Transaction]:
        """
        Retrieve transactions by type (Income or Expense).
        
        Args:
            transaction_type: The type of transactions to retrieve
            
        Returns:
            List[Transaction]: List of matching transaction objects
        """
        return self.db.query(Transaction).filter(
            Transaction.transaction_type == transaction_type
        ).all()
    
    def delete_transaction(self, transaction_id: int) -> bool:
        """
        Delete a transaction from the database.
        
        Args:
            transaction_id: The ID of the transaction to delete
            
        Returns:
            bool: True if deleted successfully, False if not found
        """
        transaction = self.get_transaction_by_id(transaction_id)
        if transaction:
            self.db.delete(transaction)
            self.db.commit()
            return True
        return False
    
    def get_transaction_summary(self) -> Dict[str, Any]:
        """
        Get a summary of all transactions.
        
        Returns:
            Dict containing summary statistics
        """
        transactions = self.db.query(Transaction).all()
        
        def is_income(t):
            return getattr(t, "transaction_type", None) == 'Income'
        
        def is_expense(t):
            return getattr(t, "transaction_type", None) == 'Expense'

        total_income = sum(t.amount for t in transactions if is_income(t))
        total_expenses = sum(t.amount for t in transactions if is_expense(t))
        net_amount = total_income - total_expenses
        
        return {
            "total_transactions": len(transactions),
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_amount": net_amount,
            "income_count": len([t for t in transactions if is_income(t)]),
            "expense_count": len([t for t in transactions if is_expense(t)])
        } 