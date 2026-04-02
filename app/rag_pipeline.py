# Chunking + Ingestion (ingestion part)
from app.embeddings import get_embedding
from app.vector_store import add_vectors

def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    
    return chunks

def ingest_document(text):
    print("Ingesting text:", text)

    chunks = chunk_text(text)
    print("✂Chunks:", chunks)

    vectors = []
    for chunk in chunks:
        emb = get_embedding(chunk)
        print("Embedding length:", len(emb))
        vectors.append(emb)

    add_vectors(vectors, chunks)
    print("Added to FAISS")

# Retrieval + Generation (query part)
from app.embeddings import get_embedding
from app.vector_store import search
from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(query):
    query_vec = get_embedding(query)
    context = search(query_vec)

    # Safety check
    if not context:
        return "No relevant data found. Please ingest documents first."

    prompt = f"""
    Context:
    {context}

    Question: {query}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content