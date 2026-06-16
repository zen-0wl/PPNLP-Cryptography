from fastapi import FastAPI

app = FastAPI(
    title="Quantum Threat Simulator",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Quantum Threat Simulator API"
    }