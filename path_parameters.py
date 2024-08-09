from fastapi import FastAPI

app = FastAPI()

'''
 Path parameters
 Path parameters are part of the URL, and FastAPI will expect them to be there.
 You declare them by adding parameters to your path operation.
 These are passed as arguments to your path operation function and you can add type annotations to them.
 The data conversion will be done for you also the data validation.
'''
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Order matters
'''
 When creating path operations, you can get to a situation where you have fixed paths. Like /users/me but also 
 paths with path parameters like /users/{user_id}.
 In those cases, you need to make sure that the fixed paths are declared first, and the paths with path parameters 
 are declared later. Otherwise, FastAPI would interpret a path like /users/me as a path parameter /users/{user_id}
'''

@app.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


# Path operations with pre-defined values for path parameters
# You can declare the possible values for a path parameter by using standard Python type hints.
# FastAPI will validate the incoming data and ensure that it matches the type hint.
# You can also use standard Python Enum classes to declare the possible values for a path parameter.
# FastAPI will validate the incoming data and ensure that it matches the Enum declaration.
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def read_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Welcome to AlexNet"}
    if model_name.value == ModelName.resnet:
        return {"model_name": model_name, "message": "Welcome to ResNet"}
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "Welcome to LeNet"}