from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.csv_parser import parse_csv
from app.services.transaction_service import TransactionService
from app.core.database import get_db


router = APIRouter()

@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Endpoint to upload a CSV file for processing.
    - Accepts only `.csv` files
    - Parses and stores transactions in database
    - Returns saved transaction data
    """
    # Check if filename exists and is a CSV file
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided.")
    
    if not file.filename.lower().endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV.")
    
    try:
        # Parse CSV data
        parsed_data = await parse_csv(file)
        
        # Save transactions to database
        transaction_service = TransactionService(db)
        saved_transactions = []
        
        for transaction_data in parsed_data:
            transaction = transaction_service.create_transaction(transaction_data)
            saved_transactions.append(transaction.to_dict())
        
        return {
            "message": f"CSV processed successfully. {len(saved_transactions)} transactions saved.",
            "transactions": saved_transactions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


@router.get("/transactions")
def get_transactions(
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve all transactions from the database.
    - Returns list of all stored transactions
    - Supports pagination with limit parameter
    """
    try:
        transaction_service = TransactionService(db)
        transactions = transaction_service.get_all_transactions(limit=limit)
        
        return {
            "transactions": [t.to_dict() for t in transactions],
            "count": len(transactions)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving transactions: {str(e)}")


@router.get("/transactions/summary")
def get_transaction_summary(db: Session = Depends(get_db)):
    """
    Get a summary of all transactions.
    - Returns total income, expenses, and net amount
    - Includes transaction counts by type
    """
    try:
        transaction_service = TransactionService(db)
        summary = transaction_service.get_transaction_summary()
        
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving summary: {str(e)}")


@router.get("/transactions/{transaction_id}")
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific transaction by ID.
    - Returns detailed transaction information
    """
    try:
        transaction_service = TransactionService(db)
        transaction = transaction_service.get_transaction_by_id(transaction_id)
        
        if not transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        
        return transaction.to_dict()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving transaction: {str(e)}")