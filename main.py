from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Buddy backend running"}

@app.get("/health")
def health():
    return {"health": "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"msg": f"Hello {name}"}
