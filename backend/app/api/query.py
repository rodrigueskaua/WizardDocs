from fastapi import APIRouter, Body, HTTPException
from services.query_service import query_knowledge_base

router = APIRouter()

@router.post("/query/")
async def query_pdf_data(body: dict = Body(...)):
  question = body.get("question")
  top_k = body.get("top_k", 5)
  provider = body.get("provider", "local")

  if not question:
    raise HTTPException(status_code=400, detail="A pergunta ('question') é obrigatória.")

  try:
    result = query_knowledge_base(question, provider=provider, top_k=top_k)
    return {
      "question": question,
      "top_k": top_k,
      "provider": provider,
      "resposta": result["resposta"],
      "fonte": result["fonte"]
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erro na consulta: {str(e)}")