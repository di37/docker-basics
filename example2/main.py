from typing import Union

from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/heros/{emp_id}")
async def get_hero(emp_id: int):

    f = open("records.json")
    data = json.load(f)
    for record in data["emp_details"]:
        if record["emp_id"] == emp_id:
            return record
    return {"Error": "Record not found!"}
