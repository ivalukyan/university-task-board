from typing import Union

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/home")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
