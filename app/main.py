from app.core.logging import setup_logging

setup_logging()

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="from-zero-to-prod")
app.include_router(router)

@app.get("/")
def health():
    return {"status": "ok"}
