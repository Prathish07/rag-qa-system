from fastapi import APIRouter
from pydantic import BaseModel
from app.rag_pipeline import generate_answer, ingest_document
from app.cache import get_cache, set_cache

router = APIRouter()

# Request Models
class IngestRequest(BaseModel):
    text: str

class QueryRequest(BaseModel):
    query: str

# Response Model (optional but clean)
class QueryResponse(BaseModel):
    answer: str
    source: str


# Ingest Endpoint
@router.post("/ingest")
def ingest(request: IngestRequest):
    ingest_document(request.text)
    return {"message": "Document ingested successfully"}


# Query Endpoint
@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    cached = get_cache(request.query)

    if cached:
        return {"answer": cached, "source": "cache"}

    answer = generate_answer(request.query)
    set_cache(request.query, answer)

    return {"answer": answer, "source": "llm"}