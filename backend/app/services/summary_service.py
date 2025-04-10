from database.mongodb import collection
from datetime import datetime

async def save_pdf_summary(filename: str, summary: str):
  doc = {
    "filename": filename,
    "summary": summary,
    "uploaded_at": datetime.now()
  }
  await collection.insert_one(doc)