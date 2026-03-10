from fastapi import FastAPI

items = []
app = FastAPI()

# GET - read data
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI REST API"}

# GET all items
@app.get("/items")
def get_items():
    return items

# POST - create item
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return {"message": "Item added", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    items[item_id] = item
    return {"message": "Item updated"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted = items.pop(item_id)
    return {"message": "Item deleted", "item": deleted}