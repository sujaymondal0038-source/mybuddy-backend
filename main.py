from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Buddy backend is alive"}

@app.get("/chat")
def chat(msg: str):
    return {"reply": f"You said: {msg}"}
