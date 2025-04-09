from database.chromadb import retrieve_relevant_chunks
from services.embedding_service import generate_embeddings_batch
from services.ai_service import ask_openai

def query_knowledge_base(question: str, provider: str = "local", top_k: int = 5):
  query_embedding = generate_embeddings_batch(question)

  if provider == "local":
    relevant_chunks = retrieve_relevant_chunks("pdf_data", query_embedding, top_k=top_k)
    
    clean_chunks = [
      {"text": ' '.join(chunk.replace("\n", " ").split()), "distance": round(distance, 4)}
      for chunk, distance in relevant_chunks
    ]
    context = " ".join(chunk["text"] for chunk in clean_chunks)
    
    return {
      "question": question,
      "resposta": context,
      "fonte": "ChromaDB",
      "top_k": top_k,
      "chunks": clean_chunks
    }

  elif provider == "openai":
    relevant_chunks = retrieve_relevant_chunks("pdf_data", query_embedding, top_k=top_k)
    
    clean_chunks = [
      {"text": ' '.join(chunk.replace("\n", " ").split()), "distance": round(distance, 4)}
      for chunk, distance in relevant_chunks
    ]
    context = " ".join(chunk["text"] for chunk in clean_chunks)
    
    resposta = ask_openai(question, context)
    return {
      "question": question,
      "resposta": resposta,
      "fonte": "OpenAI",
      "top_k": top_k,
      "chunks": clean_chunks
    }

  else:
    raise ValueError("Provedor inválido. Use 'local' ou 'openai'.")
