import datetime
from typing import Union, Annotated

<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
=======
from fastapi import Request, Depends
from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates

from models.models import User, Mailing
>>>>>>> origin/main

app = FastAPI()

templates = Jinja2Templates(directory="templates")
<<<<<<< HEAD


@app.get("/home")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})
=======


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
>>>>>>> origin/main


@app.get("/users")
async def read_item(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})


@app.get("/mailing")
async def mailing(request: Request):
    return templates.TemplateResponse("mailing.html", {"request": request})


@app.post("/mailing")
async def mail(request: Request, user_id: Annotated[str, Form()], message: Annotated[str, Form()]):
    return templates.TemplateResponse('mailing.html', {'request': request, "user_id": user_id, "message": message})


@app.get("/recordsadd")
async def recordsadd(request: Request):
    return templates.TemplateResponse('records_add.html', {'request': request})


@app.post("/recordsadd")
async def recordsadd(request: Request, subject: Annotated[str, Form()], types: Annotated[str, Form()],
                     date: Annotated[datetime.date, Form()], message: Annotated[str, Form()]):
    return templates.TemplateResponse('records_add.html',
                                      {'request': request, "subject": subject, "types": types, "date": date,
                                       "message": message})
