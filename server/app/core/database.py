"""
Database configuration and connection setup for PaySplit.AI.

This module handles:
- Database connection setup
- Session management
- Database URL configuration
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database URL - use environment variable or default to SQLite for development
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://taanishqsethi@localhost:5432/paysplit_ai"
)

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True  # Set to False in production to reduce log noise
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    """
    Database session dependency for FastAPI.
    
    Yields a database session and ensures it's closed after use.
    This is the recommended pattern for FastAPI applications.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 