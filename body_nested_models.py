from fastapi import FastAPI

app = FastAPI()

''' 
# Body - Nested Models
    We can declare Pydantic models inside other Pydantic models to create deeply nested models.
    This can be useful to model more complex JSON structures.
'''

from pydantic import BaseModel, HttpUrl, Field

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: list[str] = Field(["tags1", "tags2"], min_items=1)
    image: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer