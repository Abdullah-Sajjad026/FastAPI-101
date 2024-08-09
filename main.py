from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Union, Annotated
from pydantic import BaseModel


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


fake_items_db = [
    {"item_name": "apple", "item_price": 100},
    {"item_name": "banana", "item_price": 200},
    {"item_name": "orange", "item_price": 300},
]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users/me")
def read_me():
    return {"message": "Welcome from me"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"message": "Welcome " + str(user_id)}


@app.get("/models/{model_name}")
def read_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"message": "Welcome to AlexNet"}
    if model_name.value == ModelName.resnet:
        return {"message": "Welcome to ResNet"}
    else:
        return {"message": "Welcome to lenet"}


@app.post("/items")
def add_item(item: Item):
    return item


@app.get("/items")
def read_items(skip: int = 0, limit: int = 100):
    return {"items": fake_items_db[skip: skip + limit]}


@app.get("/items/{item_id}")
def read_item(item_id: Annotated[int, Path()], q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update(
            {"q": q}
        )
    return result
