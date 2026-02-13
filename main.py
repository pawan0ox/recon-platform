from fastapi import FastAPI
from executor import run_command

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/scan")
def scan(payload: dict):
    command = payload.get("command")
    return run_command(command)
