from pydantic import BaseModel, Field


class Joke(BaseModel):
    text: str = Field(description="The joke's text")