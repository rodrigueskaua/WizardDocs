from chromadb.config import Settings
from chromadb import Client

client = Client(Settings(
  chroma_db_impl="duckdb+parquet",
  persist_directory="/data/chromadb"
))

def store_embeddings(collection_name, texts, embeddings):
  """
  Armazena os embeddings e textos associados em uma coleção no ChromaDB.
  """
  collection = client.get_or_create_collection(name=collection_name)
  collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(texts))]
  )
  
def retrieve_relevant_chunks(collection_name, query_embedding, top_k=5):
  """
  Recupera os chunks mais relevantes do ChromaDB com base no embedding da consulta.
  """
  collection = client.get_collection(name=collection_name)
  results = collection.query(
    query_embeddings=[query_embedding],
    n_results=top_k
  )
  return results["documents"]
