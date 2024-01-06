from fastapi import FastAPI

from pydantic import BaseModel, Field

API_URL = "https://icanhazdadjoke.com/"

app = FastAPI()

@app.get("/")
async def handler():
    return {"result": "Hello 👋!"}

