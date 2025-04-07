from fastapi import APIRouter, Body, HTTPException
from services.embedding_service import generate_embeddings
from database.chromadb import retrieve_relevant_chunks

router = APIRouter()

@router.post("/query/")
async def query_pdf_data(question: str = Body(..., embed=True)):
  try:
    query_embedding = generate_embeddings(question)
    relevant_chunks = retrieve_relevant_chunks("pdf_data", query_embedding)
    return {"resposta": relevant_chunks}
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erro na consulta: {str(e)}")
