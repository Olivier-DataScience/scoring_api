from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de scoring crédit en ligne"}
