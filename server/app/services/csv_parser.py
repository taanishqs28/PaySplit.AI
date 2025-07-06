import pandas as pd
from io import StringIO
from fastapi import UploadFile

async def parse_csv(file: UploadFile) -> list:
    """
    Parses a CSV file and returns a list of transactions.
    
    Args:
        file (UploadFile): The uploaded CSV file.
    
    Returns:
        list: A list of dictionaries representing the transactions.
    """

     # Read file bytes from memory (async)
    content = await file.read()
    if not content.strip():
        return []
    #Convert bytes to a text stream so pandas can read it
    csv_data = StringIO(content.decode('utf-8'))
    
    # Read the CSV data into a DataFrame
    df = pd.read_csv(csv_data)
    
    # Convert DataFrame to a list of dictionaries
    transactions = df.where(pd.notnull(df), None).to_dict(orient='records')
    
    return transactions