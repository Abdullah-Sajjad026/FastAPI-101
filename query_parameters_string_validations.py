from fastapi import FastAPI

app = FastAPI()

'''
# Query Parameters & String Validations
    We can add many validations while declaring query parameters in path operation functions. For this reason, FastAPI provides a Query class. 
    The Query class is used to declare query parameters with validations. We can use this class with Annotated type hints.

    The Query class takes several arguments:
        default: Any = None: The default value of the query parameter.
        title: str = None: The title of the query parameter.
        description: str = None: The description of the query parameter.
        min_length: int = None: The minimum length of the query parameter.
        max_length: int = None: The maximum length of the query parameter.
        regex: str = None: The regular expression to validate the query parameter.
        alias: str = None: The alias of the query parameter.
        deprecated: bool = None: The deprecation status of the query parameter.
        gt: float = None: The minimum value of the query parameter.
        ge: float = None: The minimum value of the query parameter.
        lt: float = None: The maximum value of the query parameter.
        le: float = None: The maximum value of the query parameter.
        multiple: bool = None: The multiple status of the query parameter.
        example: Any = None: The example value of the query parameter.

    There are other classes too just like Query class e.g Path, Cookie, Header, Body, File, Form, etc. Most of these classes have similar arguments.
'''

from typing import Annotated
from fastapi import Query

@app.get("/items")
def read_items(q: Annotated[str | None, Query(
    title="Query string",
    description="Query string for the items to search in the database that have a good match",
    min_length=3,
    max_length=50,
)]):
    query_items = {"q": q}
    return query_items


'''
Defaul Values
    We can set the default value of a query parameter by assigning a value to the default argument of the Query class.
        q: str = Query("fixedquery", min_length=3)
    But in case of using Annotated type hints, we can set the default value by assigning a value to the Annotated type hint.
        q: Annotated[str | None, Query()] = "fixedquery"

Required Query Parameters
    We can make a query parameter required by setting the default value to None.
        q: str = ...
    or
        q: str = Query(..., min_length=3)
    But in case of using Annotated type hints, we can make a query parameter required by following the below syntax.
        q: Annotated[str, Query()]
    or
        q: Annotated[str, Query(..., min_length=3)] 
'''

@app.get("/items/")
def read_items(q: Annotated[str | None, Query(alias="query-item")] = "fixedquery"):
    query_items = {"q": q}
    return query_items
