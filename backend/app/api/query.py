from fastapi import APIRouter, Body, HTTPException
from services.embedding_service import generate_embeddings
from database.chromadb import retrieve_relevant_chunks

router = APIRouter()

@router.post("/query/")
async def query_pdf_data( question: str = Body(..., embed=True), top_k: int = 5):
  try:
    query_embedding = generate_embeddings(question)
    relevant_chunks = retrieve_relevant_chunks("pdf_data", query_embedding, top_k=top_k)

    return {
      "question": question,
      "top_k": top_k,
      "results": [
        {"text": chunk, "distance": round(distance, 4)}
        for chunk, distance in relevant_chunks
      ]
    }

  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erro na consulta: {str(e)}")
