from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="RAG QA System")

app.include_router(router)