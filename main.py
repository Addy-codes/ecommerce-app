from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Union

app = FastAPI()

# In-memory database for simplicity
db = [
    {"item_id": 1, "name": "Item 1", "price": 10.99, "qty": 5},
    {"item_id": 2, "name": "Item 2", "price": 19.99, "qty": 10},
    {"item_id": 3, "name": "Item 3", "price": 5.99, "qty": 2},
]


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    qty: int = Field(..., ge=0)


class ItemUpdate(BaseModel):
    name: str = Field(None, min_length=1, max_length=100)
    price: float = Field(None, gt=0)
    qty: int = Field(None, ge=0)


@app.get("/items")
async def get_items():
    return db


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    for item in db:
        if item["item_id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
async def create_item(item: ItemCreate):
    new_item = item.dict()
    new_item["item_id"] = max(item["item_id"] for item in db) + 1
    db.append(new_item)
    return {"message": "Item created"}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemUpdate):
    for db_item in db:
        if db_item["item_id"] == item_id:
            if item.name:
                db_item["name"] = item.name
            if item.price:
                db_item["price"] = item.price
            if item.qty is not None:
                db_item["qty"] = item.qty
            return {"message": "Item updated"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for item in db:
        if item["item_id"] == item_id:
            db.remove(item)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/manage_inventory")
async def manage_inventory(item_updates: List[Dict[str, Union[int, float]]]):
    for update in item_updates:
        item_id = update["item_id"]
        qty = update["qty"]

        for item in db:
            if item["item_id"] == item_id:
                if item["qty"] + qty >= 0:
                    item["qty"] += qty
                    break
                else:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Insufficient quantity for item {item_id}",
                    )
        else:
            raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

    return {"message": "Inventory updated successfully"}
