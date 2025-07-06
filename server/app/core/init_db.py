"""
Database initialization script for PaySplit.AI.

This script creates all database tables and sets up the initial database structure.
Run this script once to set up your database.
"""

from app.core.database import engine, Base
from app.models.transaction import Transaction


def init_db():
    """
    Initialize the database by creating all tables.
    
    This function creates all tables defined in your models.
    It's safe to run multiple times (tables won't be recreated if they exist).
    """
    print("Creating database tables...")
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    print("Database tables created successfully!")
    print("Available tables:")
    for table_name in Base.metadata.tables.keys():
        print(f"  - {table_name}")


if __name__ == "__main__":
    init_db() 