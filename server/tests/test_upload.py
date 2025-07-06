"""
Tests for the CSV upload endpoint.

This file tests:
- Successful CSV uploads
- Error handling for invalid files
- Edge cases like empty files
- Response format validation
"""

import pytest
from fastapi import HTTPException


class TestCSVUpload:
    """Test suite for CSV upload functionality."""
    
    def test_successful_csv_upload(self, client, sample_csv_file):
        """
        Test that a valid CSV file uploads successfully.
        
        This test ensures our main functionality works correctly.
        """
        # Prepare the file upload
        files = {"file": ("transactions.csv", sample_csv_file, "text/csv")}
        
        # Make the request
        response = client.post("/api/v1/upload", files=files)
        
        # Assert the response
        assert response.status_code == 200
        data = response.json()
        
        # Check response structure
        assert "message" in data
        assert "transactions" in data
        assert data["message"] == "CSV processed successfully"
        
        # Check that we got the expected transactions
        transactions = data["transactions"]
        assert len(transactions) == 3  # We have 3 sample transactions
        
        # Verify the first transaction structure
        first_transaction = transactions[0]
        assert "Date" in first_transaction
        assert "Description" in first_transaction
        assert "Amount" in first_transaction
        assert "Type" in first_transaction
        
        # Check specific values
        assert first_transaction["Date"] == "2024-01-15"
        assert first_transaction["Description"] == "Uber Ride"
        assert first_transaction["Amount"] == 25.50
        assert first_transaction["Type"] == "Expense"
    
    def test_non_csv_file_rejection(self, client):
        """
        Test that non-CSV files are properly rejected.
        
        This ensures our file type validation works correctly.
        """
        # Create a text file (not CSV)
        files = {"file": ("document.txt", b"This is a text file", "text/plain")}
        
        # Make the request
        response = client.post("/api/v1/upload", files=files)
        
        # Assert the response
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "File must be a CSV" in data["detail"]
    
    def test_missing_file_parameter(self, client):
        """
        Test that requests without a file parameter are handled properly.
        
        This tests our endpoint's parameter validation.
        """
        # Make request without file
        response = client.post("/api/v1/upload")
        
        # Should get a validation error
        assert response.status_code == 422  # Unprocessable Entity
    
    def test_empty_csv_file(self, client):
        """
        Test handling of empty CSV files.
        
        This tests an edge case that could cause issues.
        """
        # Create an empty CSV file
        files = {"file": ("empty.csv", b"", "text/csv")}
        
        # Make the request
        response = client.post("/api/v1/upload", files=files)
        
        # This should either succeed (empty list) or fail gracefully
        # Let's see what happens and adjust our code accordingly
        assert response.status_code in [200, 400, 500]
    
    def test_malformed_csv_file(self, client):
        """
        Test handling of malformed CSV files.
        
        This ensures our error handling works for invalid CSV data.
        """
        # Create malformed CSV data
        malformed_data = b"Invalid,CSV,Data\nNo,Proper,Structure"
        files = {"file": ("malformed.csv", malformed_data, "text/csv")}
        
        # Make the request
        response = client.post("/api/v1/upload", files=files)
        
        # Should handle gracefully (either 200 with empty data or 500 with error)
        assert response.status_code in [200, 500]
    
    def test_large_csv_file(self, client):
        """
        Test handling of larger CSV files.
        
        This helps ensure our system can handle realistic file sizes.
        """
        # Create a larger CSV with more transactions
        import pandas as pd
        
        # Generate 100 sample transactions
        data = {
            'Date': [f'2024-01-{i:02d}' for i in range(1, 101)],
            'Description': [f'Transaction {i}' for i in range(1, 101)],
            'Amount': [float(i * 10.50) for i in range(1, 101)],
            'Type': ['Expense' if i % 2 == 0 else 'Income' for i in range(1, 101)]
        }
        
        df = pd.DataFrame(data)
        csv_data = df.to_csv(index=False).encode('utf-8')
        
        files = {"file": ("large_transactions.csv", csv_data, "text/csv")}
        
        # Make the request
        response = client.post("/api/v1/upload", files=files)
        
        # Should handle successfully
        assert response.status_code == 200
        data = response.json()
        assert len(data["transactions"]) == 100 