import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

def store_embeddings(collection_name, texts, embeddings):
  collection = client.get_or_create_collection(name=collection_name)
  collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(texts))]
  )

def retrieve_relevant_chunks(collection_name, query_embedding, top_k=5):
  collection = client.get_collection(name=collection_name)
  results = collection.query(
    query_embeddings=[query_embedding],
    n_results=top_k
  )
  return results["documents"]
