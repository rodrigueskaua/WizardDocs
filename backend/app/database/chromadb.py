from typing import List, Tuple
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

def store_embeddings(collection_name, texts, embeddings):
  collection = client.get_or_create_collection(name=collection_name)
  collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(texts))]
  )

def retrieve_relevant_chunks(
  collection_name: str,
  query_embedding: List[float],
  top_k: int = 5
) -> List[Tuple[str, float]]:
  collection = client.get_collection(name=collection_name)

  results = collection.query(
    query_embeddings=[query_embedding],
    n_results=top_k
  )

  documents = results.get("documents", [[]])[0]
  distances = results.get("distances", [[]])[0]

  return list(zip(documents, distances))
