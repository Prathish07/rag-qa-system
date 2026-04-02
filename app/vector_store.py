import faiss
import numpy as np

dimension = 1536
index = faiss.IndexFlatL2(dimension)
documents = []

def add_vectors(vectors, texts):
    global documents
    index.add(np.array(vectors).astype('float32'))
    documents.extend(texts)

def search(query_vector, k=3):
    D, I = index.search(np.array([query_vector]).astype('float32'), k)
    return [documents[i] for i in I[0]]