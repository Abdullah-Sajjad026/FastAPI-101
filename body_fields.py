from fastapi import FastAPI

app = FastAPI()

'''
# Body - Fields
    Just like Path, Query, Body, we can set validations on Pydantic models' fields using Field from pydantic.
'''
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., title="The name of the item", min_length=3, max_length=50, example="Awesome Item")
    description: str = Field(None, title="The description of the item", max_length=100, example="This is an awesome item")
    price: float = Field(..., title="The price of the item", gt=0, )
    tax: float = Field(None, title="The tax rate of the item", ge=0, le=10)

@app.post("/items/")
async def create_item(item: Item):
    return item