from fastapi import FastAPI, Request

from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
async def handler():
    return {"result": "Hello 👋!"}


class Joke(BaseModel):
    text: str = Field(description="The joke's text")


@app.post("/api/gpt", description="Returns a random joke")
async def handler_gpt(req: Request) -> Joke:
    print(await req.json())
    return Joke(
        text="Hear about the new restaurant called Karma? There's no menu: You get what you deserve."
    )
