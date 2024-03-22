from fastapi import FastAPI
from pydantic import BaseModel, Field
import datetime as pydatetime
import json

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

def get_now():
    temptime = pydatetime.datetime.now()
    return temptime.timestamp()


class Product(BaseModel):
    id: str | None ='prod_01HS87EW3PBFTGCF8BQF524TQA'
    title: str | None = 'roopy'
    subtitle: str | None = '루피'
    description: str | None = '귀여운 인형 可爱的娃娃'
    handle: str | None = 'roopy'
    is_giftcard: bool | None = None
    thumbnail: str | None = 'http://localhost:9000/uploads/1710747780504-roopy.jpeg'
    weight:  int | None = 400
    length:  int | None = 123
    height: int | None = 456
    width: int | None = 789
    hs_code: str | None = None
    origin_country: str | None = None
    mid_code: str | None = None
    material: str | None = None
    created_at:  float | None = get_now()
    updated_at: float | None = get_now()
    deleted_at: float | None = get_now()
    metadata: str | None ='{"img_url":"s3.aws.com" }'
    collection_id: str | None = 'pcol_01HS87EVYMDVX1FJZJ2JQ2GP16'
    type_id: str | None = None
    discountable: str | None = None
    status: str | None = 'published'
    external_id: str | None = None



app = FastAPI(title='sourcingroot API Swagger')



@app.post("/Product")
async def create_product(item: Product):
    return item

@app.get("/Product")
async def view_product(item: Product):
    return item


@app.get("/GqMain")
async def view_product(item: Product):
    return item

@app.post("/GqMain")
async def view_product(item: Product):
    return item

@app.get("/GqList")
async def view_product(item: Product):
    return item

@app.get("/GqView")
async def view_product(item: Product):
    return item

@app.get("/GqWrite")
async def view_product(item: Product):
    return item

@app.get("/GqState")
async def view_product(item: Product):
    return item

@app.get("/store")
async def view_product(item: Product):
    return item

@app.post("/store")
async def view_product(item: Product):
    return item

@app.post("/login/")
async def create_item(item: Item):
    return item

@app.post("/logout/")
async def create_item(item: Item):
    return item

@app.get("/clause/")
async def create_item(item: Item):
    return item