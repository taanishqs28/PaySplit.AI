"""
Unit tests for the CSV parser service.

This file tests the business logic of CSV parsing independently
from the HTTP layer. This is important for:
- Isolating bugs to specific components
- Making tests faster and more reliable
- Ensuring our parsing logic works correctly
"""

import pytest
import pandas as pd
from io import BytesIO
from unittest.mock import AsyncMock

from app.services.csv_parser import parse_csv


class TestCSVParser:
    """Test suite for CSV parsing functionality."""
    
    @pytest.mark.asyncio
    async def test_parse_valid_csv(self):
        """
        Test parsing a valid CSV file.
        
        This tests the core functionality of our CSV parser.
        """
        # Create sample CSV data
        data = {
            'Date': ['2024-01-15', '2024-01-16'],
            'Description': ['Uber Ride', 'Starbucks'],
            'Amount': [25.50, 4.75],
            'Type': ['Expense', 'Expense']
        }
        
        df = pd.DataFrame(data)
        csv_content = df.to_csv(index=False)
        
        # Create a mock UploadFile
        mock_file = AsyncMock()
        mock_file.read.return_value = csv_content.encode('utf-8')
        
        # Parse the CSV
        result = await parse_csv(mock_file)
        
        # Assertions
        assert isinstance(result, list)
        assert len(result) == 2
        
        # Check first transaction
        first_transaction = result[0]
        assert first_transaction['Date'] == '2024-01-15'
        assert first_transaction['Description'] == 'Uber Ride'
        assert first_transaction['Amount'] == 25.50
        assert first_transaction['Type'] == 'Expense'
    
    @pytest.mark.asyncio
    async def test_parse_empty_csv(self):
        """
        Test parsing an empty CSV file.
        
        This tests how our parser handles edge cases.
        """
        # Create empty CSV
        csv_content = ""
        
        # Create a mock UploadFile
        mock_file = AsyncMock()
        mock_file.read.return_value = csv_content.encode('utf-8')
        
        # Parse the CSV
        result = await parse_csv(mock_file)
        
        # Should return empty list
        assert isinstance(result, list)
        assert len(result) == 0
    
    @pytest.mark.asyncio
    async def test_parse_csv_with_different_columns(self):
        """
        Test parsing CSV with different column names.
        
        This ensures our parser is flexible and can handle
        various CSV formats that users might upload.
        """
        # Create CSV with different column names
        data = {
            'Transaction_Date': ['2024-01-15'],
            'Merchant': ['Uber'],
            'Transaction_Amount': [25.50],
            'Category': ['Transportation']
        }
        
        df = pd.DataFrame(data)
        csv_content = df.to_csv(index=False)
        
        # Create a mock UploadFile
        mock_file = AsyncMock()
        mock_file.read.return_value = csv_content.encode('utf-8')
        
        # Parse the CSV
        result = await parse_csv(mock_file)
        
        # Should handle different column names gracefully
        assert isinstance(result, list)
        assert len(result) == 1
        
        # Check that we preserve the original column names
        transaction = result[0]
        assert 'Transaction_Date' in transaction
        assert 'Merchant' in transaction
        assert 'Transaction_Amount' in transaction
        assert 'Category' in transaction
    
    @pytest.mark.asyncio
    async def test_parse_csv_with_missing_values(self):
        """
        Test parsing CSV with missing/empty values.
        
        This tests how pandas handles NaN values and ensures
        our parser doesn't break with incomplete data.
        """
        # Create CSV with missing values
        data = {
            'Date': ['2024-01-15', '2024-01-16', '2024-01-17'],
            'Description': ['Uber Ride', '', 'Freelance Payment'],
            'Amount': [25.50, None, 500.00],
            'Type': ['Expense', 'Expense', '']
        }
        
        df = pd.DataFrame(data)
        csv_content = df.to_csv(index=False)
        
        # Create a mock UploadFile
        mock_file = AsyncMock()
        mock_file.read.return_value = csv_content.encode('utf-8')
        
        # Parse the CSV
        result = await parse_csv(mock_file)
        
        # Should handle missing values
        assert isinstance(result, list)
        assert len(result) == 3
        
        # Check that missing values are handled properly
        # (pandas will convert them to NaN, which becomes None in JSON)
        assert pd.isna(result[1]['Description'])
        assert result[1]['Amount'] is None or pd.isna(result[1]['Amount'])
        assert result[2]['Type'] in (None,'')
    
    @pytest.mark.asyncio
    async def test_parse_csv_with_unicode_characters(self):
        """
        Test parsing CSV with unicode characters.
        
        This ensures our parser handles international characters
        and special symbols correctly.
        """
        # Create CSV with unicode characters
        data = {
            'Date': ['2024-01-15'],
            'Description': ['Café & Restaurant 🍕'],
            'Amount': [45.99],
            'Type': ['Expense']
        }
        
        df = pd.DataFrame(data)
        csv_content = df.to_csv(index=False)
        
        # Create a mock UploadFile
        mock_file = AsyncMock()
        mock_file.read.return_value = csv_content.encode('utf-8')
        
        # Parse the CSV
        result = await parse_csv(mock_file)
        
        # Should handle unicode correctly
        assert isinstance(result, list)
        assert len(result) == 1
        
        transaction = result[0]
        assert transaction['Description'] == 'Café & Restaurant 🍕'
        assert transaction['Amount'] == 45.99 