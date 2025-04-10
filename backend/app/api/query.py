from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from services.query_service import query_knowledge_base
from datetime import datetime

router = APIRouter()

@router.post("/query/")
async def query_pdf_data(body: dict = Body(...)):
  question = body.get("question")
  top_k = body.get("top_k", 5)
  provider = body.get("provider", "local")

  if not question:
    return JSONResponse(
      status_code=status.HTTP_400_BAD_REQUEST,
      content={
        "message": "Requisição inválida.",
        "error": "A chave 'question' é obrigatória no corpo da requisição."
      }
    )

  try:
    result = query_knowledge_base(question, provider=provider, top_k=top_k)
    
    return JSONResponse(
      status_code=status.HTTP_200_OK,
      content={
        "success": True,
        "summary": {
          "answer": result["answer"],
          "source": result["source"],
          "top_k_used": result["top_k"],
          "retrieved_chunks": result["chunks"]
        },
        "meta": {
          "query": result["question"],
          "retrieved_at": datetime.utcnow().isoformat() + "Z"
        }
      }
    )
  except Exception as e:
    return JSONResponse(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      content={
        "message": "Erro interno.",
        "error": str(e)
      }
    )