from fastapi import FastAPI
from app.routers import eoq_router

app = FastAPI(title="Smart Inventory AI - ML Service")

# S1-03: Health Endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

# Connect your future routers here
app.include_router(eoq_router.router)