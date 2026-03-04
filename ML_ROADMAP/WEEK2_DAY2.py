from fastapi import FastAPI
app = FastAPI()
items={}
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