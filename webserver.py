import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class Example001(BaseModel):
    name: str


class Example002(BaseModel):
    list_of_names: List[str]


class Example003(BaseModel):
    example001: Example001
    example002: Example002


class DishDetails(BaseModel):
    food_name: str
    food_amount: int


class Detail(BaseModel):
    dish_name: str
    dish_details: DishDetails


class Item(BaseModel):
    time: Union[str, datetime]
    details: List[Detail]


app = FastAPI()
p = Path('db.json')
with p.open('r') as file:
    file_data = file.read()
    meals: List = json.loads(file_data) if file_data else []


@app.get('/')
async def root():
    return {"message": "Hello Anton!"}


@app.get("/list")
async def list_of_meals():
    result = []
    for index, meal_ in enumerate(meals):
        result.append({f'{index + 1}': meal_})
    return {"meals": result}


@app.get("/meal/{item_id}")
async def meal(item_id: int):
    return {f"meal[{item_id}]": meals[int(item_id) - 1]} if item_id in range(1, len(meals) + 1) else {
        "error": f"id [{item_id}] out of range [1:{len(meals)}]"}


@app.post("/create")
async def create_item(item: Item):
    # преобраховать данные из item в формат данных из db.json
    # добавить преобразованные данные в expenses

    details = {'name': item.details[0].dish_name,
               'food': item.details[0].dish_details.food_name,
               'amount': item.details[0].dish_details.food_amount}
    time_value = datetime.now() if item.time == 'now' else item.time
    meals.append({time_value: details})
    return item


@app.post("/Example001")
async def example(item: Example001):
    return item


@app.post("/Example002")
async def example(item: Example002):
    return item


@app.post("/Example003")
async def example(item: Example003):
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    sys.exit(0)
