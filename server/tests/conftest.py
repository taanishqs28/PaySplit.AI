"""
Test configuration and shared fixtures for PaySplit.AI tests.

This file contains:
- Test client setup
- Sample CSV data for testing
- Common fixtures used across multiple test files
"""

import pytest
from fastapi.testclient import TestClient
from io import BytesIO
import pandas as pd

from app.main import app


@pytest.fixture
def client():
    """
    Create a test client for the FastAPI application.
    
    This fixture provides a way to make HTTP requests to your app
    without actually starting a server. Perfect for unit testing!
    """
    return TestClient(app)


@pytest.fixture
def sample_csv_data():
    """
    Create sample CSV data for testing file uploads.
    
    This fixture provides realistic transaction data that we can use
    to test our CSV parsing functionality.
    """
    # Sample transaction data that a user might upload
    data = {
        'Date': ['2025-06-20', '2025-06-21', '2025-06-22'],
        'Description': ['Uber Ride', 'Starbucks Coffee', 'Freelance Payment'],
        'Amount': [25.50, 4.75, 500.00],
        'Type': ['Income', 'Expense', 'Expense']
    }
    
    # Create a DataFrame and convert to CSV string
    df = pd.DataFrame(data)
    csv_string = df.to_csv(index=False)
    
    return csv_string


@pytest.fixture
def sample_csv_file(sample_csv_data):
    """
    Create a file-like object with sample CSV data.
    
    This simulates what FastAPI receives when a user uploads a file.
    """
    return BytesIO(sample_csv_data.encode('utf-8'))


@pytest.fixture
def malformed_csv_data():
    """
    Create malformed CSV data to test error handling.
    
    This helps us ensure our app gracefully handles bad input.
    """
    return "This is not a valid CSV file\nIt has no proper structure"


@pytest.fixture
def empty_csv_data():
    """
    Create an empty CSV file to test edge cases.
    """
    return "" 