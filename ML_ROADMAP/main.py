from fastapi import FastAPI

## Here what actuatlly happens is that we are telling python to look fora a file called __init__.py in fastapi package from where we can access the FastAPI class present in the application.py file

# app=FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello":"World"}

# @app.get("/items/{item_id}")
# def read_item(item_id:int, q:str=None): 
#     return {"item_id":item_id, "q":q}
from fastapi import FastAPI

app = FastAPI()

items = {}   


@app.post("/items/")
def create_item(item_id: int, q: str = None):
    items[item_id] = q
    return {"message": "Item stored"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "q": items.get(item_id)}

@app.get("/items/")
def read_all_items():
    return items