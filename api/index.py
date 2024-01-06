from contextlib import asynccontextmanager
from typing import Annotated, List
from fastapi import Depends, FastAPI, Path, Request
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


