from fastapi import FastAPI

app = FastAPI()

'''
# Body - Multiple Parameters
   We can declare multiple body parameters in a path operation function by using Pydantic models. The body parameters can be declared in the path operation function as function parameters.
'''
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None

@app.post("/items/")
async def create_item(item: Item, user: User):
    return {"item": item, "user": user}

'''
    FastAPI will notice that there are more than one body parameters in the function (two parameters that are Pydantic models).
    So, it will then use the parameter names as keys (field names) in the body, and expect a body like:
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "dave",
            "full_name": "Dave Grohl"
        }
    }

    We could decide that we want to have another key importance in the same body, besides the item and user.
    If we declare it as is, because it is a singular value, FastAPI will assume that it is a query parameter.
    But we can instruct FastAPI to treat it as another body key using Body
'''
from fastapi import Body

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body(...)):
    result = {"item_id": item_id, **item.dict(), "user": user.dict(), "importance": importance}
    return result