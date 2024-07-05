from typing import Union

from fastapi import Request
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from src import models


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/users")
async def read_item(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})
