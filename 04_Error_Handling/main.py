from fastapi import FastAPI,Path,Query,HTTPExceptionsHandler
from typing import Union
from enum import Enum
from pydantic import BaseModel
from unittest.util import _MAX_LENGTH


app : FastAPI = FastAPI()

items = [1,2,3,4]

@app.get('/error/handler')
async def error_handler(item: int):
    if item not in items:
        return HTTPExceptionsHandler(status_code=404,detail="Item not found")
    return {"item": item}

