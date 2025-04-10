from fastapi import APIRouter, UploadFile, HTTPException
from services.pdf_service import extract_text_from_pdf, split_text_into_chunks
from services.embedding_service import generate_embeddings_batch
from services.ai_service import generate_summary
from services.summary_service import save_pdf_summary
from database.chromadb import store_embeddings

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile):
  if file.content_type != "application/pdf":
    raise HTTPException(status_code=400, detail="O arquivo deve ser um PDF.")

  try:
    text = extract_text_from_pdf(file.file)
    chunks = split_text_into_chunks(text)

    if not chunks:
      raise HTTPException(status_code=422, detail="O PDF não contém texto processável.")

    # Gerar embeddings em batch
    embeddings = generate_embeddings_batch(chunks)

    # Armazenar no banco vetorial
    store_embeddings(collection_name="pdf_data", texts=chunks, embeddings=embeddings)

    summary = await generate_summary(chunks, num_chunks=5)
    await save_pdf_summary(file.filename, summary)
    
    return {
      "message": "PDF processado e armazenado com sucesso!",
      "total_chunks": len(chunks)
    }

  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erro ao processar o PDF: {str(e)}")
