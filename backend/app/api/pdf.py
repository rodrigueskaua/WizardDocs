from fastapi import APIRouter, UploadFile, HTTPException
from app.services.pdf_service import extract_text_from_pdf, split_text_into_chunks
from app.services.embedding_service import generate_embeddings
from app.database.chromadb import store_embeddings

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile):
  # Verificar se o arquivo é um PDF
  if file.content_type != "application/pdf":
    raise HTTPException(status_code=400, detail="O arquivo deve ser um PDF.")
  
  try:
    text = extract_text_from_pdf(file.file)
    
    chunks = split_text_into_chunks(text)
    
    # Gerar embeddings
    embeddings = [generate_embeddings(chunk) for chunk in chunks]
    
    # Armazenar embeddings no banco vetorial
    store_embeddings(collection_name="pdf_data", texts=chunks, embeddings=embeddings)
    
    return {"message": "PDF processado e armazenado com sucesso!"}
  
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erro ao processar o PDF: {str(e)}")
