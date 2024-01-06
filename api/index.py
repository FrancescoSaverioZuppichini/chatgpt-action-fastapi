from fastapi import FastAPI, Request

from lib.schemas import Joke


app = FastAPI()


@app.get("/")
async def handler():
    return {"hello": "there!"}


@app.post("/api/gpt", description="Returns a random joke", response_model=Joke)
async def handler_gpt(req: Request):
    print(await req.json())
    return Joke(
        text="Hear about the new restaurant called Karma? There's no menu: You get what you deserve."
    )
