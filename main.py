from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "Buddy backend is running"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Buddy, my personal AI friend and assistant."},
            {"role": "user", "content": req.message}
        ]
    )
    return {
        "reply": response["choices"][0]["message"]["content"]
    }
