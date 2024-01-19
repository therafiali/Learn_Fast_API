from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validate the user's username and password
    # For now, we'll assume any user is valid
    return {"access_token": form_data.username, "token_type": "bearer"}


@app.post("/generate_token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    print("form_data",form_data)
    return {"access_token": form_data.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(token:str = Depends(oauth2_scheme)):
    print("token",token)
    return{
        "user":"Rafi Ali",
        "age":22
    }