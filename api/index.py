from contextlib import asynccontextmanager
from typing import Annotated, List
from fastapi import Depends, FastAPI, Path, Request
import httpx
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/api")
async def root():
    return {"message": "Hello World"}