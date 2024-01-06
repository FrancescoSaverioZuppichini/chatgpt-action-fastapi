from fastapi import FastAPI

from pydantic import BaseModel, Field

API_URL = "https://icanhazdadjoke.com/"

app = FastAPI()

@app.get("/api")
async def handler():
    return {"result": "Hello 👋!"}

