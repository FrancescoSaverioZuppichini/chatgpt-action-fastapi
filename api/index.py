from fastapi import FastAPI, Request
from pydantic import BaseModel, Field

app = FastAPI()

class Joke(BaseModel):
    text: str = Field(description="The joke's text")

@app.post("/api/gpt", description="Returns a random joke", response_model=Joke)
async def root(req: Request):
    print(await req.json())
    return Joke(text="Hear about the new restaurant called Karma? There's no menu: You get what you deserve.") 