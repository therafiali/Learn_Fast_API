from fastapi import FastAPI,Path,Query
from typing import Union
from enum import Enum
from pydantic import BaseModel
from unittest.util import _MAX_LENGTH

app : FastAPI = FastAPI()

@app.get("/item/{item}")
def path_func(item):
    name = {"path": item}
    return name
   
@app.get("/query")
def query_func(name: Union[str, None] = None, roll_no: Union[str, None] = Query(default=None, min_lenght=3,max_lenght=4)):
    data = {"name": name, "roll_no": roll_no}
    return data

class Choice_Name(str, Enum):
    name1 = "name1"
    name2 = "name2"
    name3 = "name3"
    
@app.get("/choice")
async def choice_func(name: Choice_Name):
    if name == Choice_Name.name1:
        return {"name": name}
    elif name == Choice_Name.name2:
        return {"name": name}
    else:
        return {"name": name}    
    
class schema1(BaseModel):
    name: str
    roll_no: int
    Class: str    
    
    
#request body    
@app.post("/items/")
async def create_item(item: schema1):
    return item    
    