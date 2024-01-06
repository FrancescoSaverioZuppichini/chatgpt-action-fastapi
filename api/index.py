from contextlib import asynccontextmanager
from fastapi import FastAPI
import httpx
from pydantic import BaseModel, Field

API_URL = "https://icanhazdadjoke.com/"

app = FastAPI()

class Joke(BaseModel):
    text: str = Field(description="The joke's text")

@app.get("/")
async def handler():
    return {"result": "Hello 👋!"}

# @app.get("/api/jokes/random", description="Returns a random joke")
# async def handler_gpt() -> Joke:
#     headers = {
#         "Accept": "application/json",
#         "User-Agent": "My FastAPI app (https://myapp.com/contact)",
#     }
#     async with httpx.AsyncClient() as client:
#         resp = await client.get(API_URL, headers=headers)
#     data = resp.json()
#     return Joke(text=data["joke"])

# @app.get("/api/jokes/search")
# async def search_jokes(
#     term: str,
#     page: int = 0,
# ) -> list[Joke]:
#     url = f"{API_URL}/search?term={term}&page={page}&limit={20}"
#     headers = {
#         "Accept": "application/json",
#         "User-Agent": "My FastAPI app (https://myapp.com/contact)",
#     }
#     async with httpx.AsyncClient() as client:
#         resp = await client.get(url, headers=headers)
#     data = resp.json()
#     return [Joke(text=joke["joke"]) for joke in data["results"]]
