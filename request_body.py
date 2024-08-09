from fastapi import FastAPI

app = FastAPI()

'''
Request body
    When you declare a Pydantic model in a path operation, FastAPI will use it to parse the body of the request.
    The body of the request needs to be a JSON object.
    FastAPI will read the body, convert it to the type of the Pydantic model, and pass it to the path operation function.
    If the body is invalid JSON, FastAPI will respond with an error.
    If the body is valid JSON but doesn't match the type of the Pydantic model, FastAPI will respond with an error.
    If the body is valid JSON and matches the type of the Pydantic model, FastAPI will parse it and pass it to the path operation function.
'''

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

'''
# Request Body, Path Parameters, Query Parameters
'''

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str = None):
    result = {
        "item_id": item_id, 
        **item.model_dump()
    }
    if q:
        result.update({"q": q})
    return result