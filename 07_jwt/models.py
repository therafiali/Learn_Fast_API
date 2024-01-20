from pydantic import BaseModel

class Token(BaseModel):
    """ access_token:str, token_type: str """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """ username: str | None = None """
    username: str | None = None


class User(BaseModel):
    """ username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None """
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    """inherit User & hashed_password: str"""
    hashed_password: str