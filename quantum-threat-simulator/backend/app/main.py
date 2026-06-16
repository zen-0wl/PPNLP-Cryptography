from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.lwe_routes import router as lwe_router
from app.api.classical_routes import router as classical_router

app = FastAPI(
    title="Quantum Threat Simulator",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Quantum Threat Simulator API"
    }

app.include_router(lwe_router)
app.include_router(classical_router)