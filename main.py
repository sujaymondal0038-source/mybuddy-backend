from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Buddy backend is running"}
