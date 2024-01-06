from contextlib import asynccontextmanager
from typing import Annotated, List
from fastapi import Depends, FastAPI 
import httpx
from pydantic import BaseModel, Field

API_URL = "https://icanhazdadjoke.com/"


class HTTPClient:
    client: httpx.AsyncClient = None

    @classmethod
    async def get_client(cls):
        if cls.client is None:
            cls.client = httpx.AsyncClient()
        return cls.client


async def get_http_client():
    return await HTTPClient.get_client()


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    if HTTPClient.client:
        await HTTPClient.client.aclose()


app = FastAPI(lifespan=lifespan)
client = httpx.AsyncClient()

HTTPClientDeps = Annotated[httpx.AsyncClient, Depends(get_http_client)]


@app.get("/")
async def handler():
    return {"result": "Hello 👋!"}


class Joke(BaseModel):
    text: str = Field(description="The joke's text")


@app.get("/api/jokes/random", description="Returns a random joke")
async def handler_gpt(
    http_client: HTTPClientDeps,
) -> Joke:
    headers = {
        "Accept": "application/json",
        "User-Agent": "My FastAPI app (https://myapp.com/contact)",
    }
    resp = await http_client.get(API_URL, headers=headers)
    data = resp.json()
    return Joke(text=data["joke"])


@app.get("/api/jokes/search")
async def search_jokes(
    http_client: HTTPClientDeps,
    term: str,
    page: int = 0,
) -> List[Joke]:
    url = f"{API_URL}/search?term={term}&page={page}&limit={20}"
    headers = {
        "Accept": "application/json",
        "User-Agent": "My FastAPI app (https://myapp.com/contact)",
    }
    resp = await http_client.get(url, headers=headers)
    data = resp.json()
    return [Joke(text=joke["joke"]) for joke in data["results"]]
