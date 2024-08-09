from fastapi import FastAPI

app = FastAPI()

'''
Path Parameters Validation
    We can add many validations while declaring path parameters in path operation functions. For this reason, FastAPI provides a Path class. 
    The Path class is used to declare path parameters with validations. We can use this class with Annotated type hints.

    There are other classes too just like Path class e.g Query, Cookie, Header, Body, File, Form, etc. Most of these classes have similar arguments.
'''
from fastapi import Path

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="The ID of the item to get", ge=1)):
    return {"item_id": item_id}

# With Annotated
from typing import Annotated
from fastapi import Query

@app.get("/items/{item_id}")
def read_item(item_id: Annotated[int, Path( title="The ID of the item to get", ge=1)], q: Annotated[str, Query(..., min_length=3, example="awesome-item")] = "abc"):
    return {"item_id": item_id}