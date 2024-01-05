from fastapi import FastAPI,Path,Query,Form,File,UploadFile
from typing import Union
from enum import Enum
from pydantic import BaseModel
from unittest.util import _MAX_LENGTH

app : FastAPI = FastAPI()

class MyList(BaseModel):
    one:str
    two:str
    three:str

@app.post("/form/data")
async def formdata(items: MyList):
    return ({"items": items})

# @app.post("/form/data")
# async def formdata(username:str = Form(), password:str = Form()):
#     return ({"username": username,"password": password})

@app.post("/file/upload")
async def formfile(file: bytes = File()):
    return ({"file": len(file)})


@app.post("/upload/file")
async def formfile(file: UploadFile):
    return ({"file": file,"file Content": file.content_type})



@app.post("/upload/file/data")
async def form_data_file(file: UploadFile,filesize: bytes = File(), name:str = Form()):
    return ({"file name": file.filename,"file Size": len(filesize),"name":name})