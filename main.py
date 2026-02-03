from fastapi import FastAPI
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Buddy backend running"}

@app.post("/chat")
def chat(msg: str):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=msg
    )
    return {"reply": response.output_text}
