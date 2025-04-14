import os
import pandas as pd
from pypdf import PdfReader


def find_file_type(name):
    _, ext = os.path.splitext(name.lower())
    if ext in ['.xlsx', '.xls']:
        return 'excel'
    elif ext in ['.csv']:
        return 'csv'
    elif ext in ['.pdf']:
        return 'pdf'
    elif ext in ['.doc', '.docx']:
        return 'word'
    elif ext in ['.jpg', '.jpeg', '.png']:
        return 'image'
    elif ext in ['.txt']:
        return 'text'
    else:
        return 'unknown'
    
def read_file(file, file_type):
    df = None
    expected_columns = ['SN', 'Unit Code', 'Floor', 'Unit Type', 'Asking Price', \
               '20% DP-50%-30%', '50% DP-20%-30%', '70% DP-30%', 'Full Payment', \
                'TotalArea', 'NetArea', 'TerraceArea', 'View']

    if file_type == "excel":
        df = pd.read_excel(file, skiprows=2)
    elif file_type == "image":
        raise Exception("File quality low")
    elif file_type == "pdf":
        raise Exception("File quality low")
    if df is None or df.empty:
        raise Exception("File Type Doesn't Match")
    
    df.columns = df.columns.str.strip()
    if list(df.columns) != expected_columns:
        raise Exception("Columns do not match the expected columns")

    return df.to_dict(orient="records")
