from database.chromadb import retrieve_relevant_chunks
from services.embedding_service import generate_embeddings
from services.ai_service import ask_openai

def query_knowledge_base(question: str, provider: str = "local", top_k: int = 5):
  query_embedding = generate_embeddings(question)

  if provider == "local":
    relevant_chunks = retrieve_relevant_chunks("pdf_data", query_embedding, top_k=top_k)
    context = "\n".join([chunk for chunk, _ in relevant_chunks])
    return {"resposta": context, "fonte": "ChromaDB"}

  elif provider == "openai":
    relevant_chunks = retrieve_relevant_chunks("pdf_data", query_embedding, top_k=top_k)
    context = "\n".join([chunk for chunk, _ in relevant_chunks])
    resposta = ask_openai(question, context)
    return {"resposta": resposta, "fonte": "OpenAI"}

  else:
    raise ValueError("Provedor inválido. Use 'local' ou 'openai'.")
