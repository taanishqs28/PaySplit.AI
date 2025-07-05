from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.csv_parser import parse_csv


router = APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    """
    Endpoint to upload a CSV file for processing.
    - Accepts only `.csv` files
    - Returns parsed transaction data
    """
    if not file.filename.lower().endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV.")
    
    try:
        data = await parse_csv(file)
        return {"message": "CSV processed successfully", "transactions": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")