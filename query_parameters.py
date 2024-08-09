from fastapi import FastAPI

app = FastAPI()

'''
Query parameters
 When you declare other function parameters that are not part of the path parameters, they are interpreted as query parameters.
'''

@app.get("/items/")
def read_item(skip: int = 0, limit: int  = 10):
    return {"skip": skip, "limit": limit}

'''
# Optional query parameters
    We can declare query parameters to be optional by setting a default value for them
    In this case, the query parameter q is optional, and if it is not provided, FastAPI will set it to None.

# Query parameters with type conversion and validation
 You can declare the type of a query parameter by adding a type annotation.
 FastAPI will use the type annotation to convert the incoming data.
 If the data can't be converted, FastAPI will respond with a validation error.
 In this case, the query parameter q is declared to be of type str.
 FastAPI will convert the incoming data to a string.

# Multiple path and query parameters
    You can declare multiple path and query parameters.
    FastAPI will match the parameters by name.
    In this case, the path parameter item_id is matched with the path parameter in the URL.
    The query parameter q is matched with the query parameter in the URL.
'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}
