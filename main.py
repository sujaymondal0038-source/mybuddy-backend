from fastapi import FastAPI
import os
import openai

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Buddy backend is alive"}

@app.get("/test")
def test():
    return {"msg": "Hello from Buddy"}

@app.get("/ask")
def ask(q: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        return {"error": "No API key found"}

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Buddy, my personal AI assistant"},
            {"role": "user", "content": q}
        ]
    )
    return {"reply": response["choices"][0]["message"]["content"]}
