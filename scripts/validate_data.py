# scripts/validate_data.py
import pandas as pd
import PyPDF2

def validate_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"CSV loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"Columns: {list(df.columns)}")
        print(f"Sample data:\n{df.head(3)}")
        return True
    except Exception as e:
        print(f"CSV validation failed: {e}")
        return False

def validate_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            first_page_text = pdf_reader.pages[0].extract_text()[:200]
            print(f"PDF loaded successfully: {num_pages} pages")
            print(f"First 200 chars: {first_page_text}")
            return True
    except Exception as e:
        print(f"PDF validation failed: {e}")
        return False

validate_csv('data/forecast.csv')
validate_pdf('data/earnings_report.pdf')
