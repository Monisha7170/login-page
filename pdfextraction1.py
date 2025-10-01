import os
import fitz # PyMuPDF for PDF
from docx import Document
def extract_text_from_pdf(pdf_path):
    text=""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
            return text.strip()
    except Exception as e:
        return f"[ERROR] Could not extract PDF: {str(e)}"
    
pdf_path = input("Enter the path of the PDF: ").strip('"')   # 👈 here
print(extract_text_from_pdf(pdf_path))