from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models import  TokenData, User, UserInDB
from data import fake_users_db
from jose import JWTError, jwt
from passlib.context import CryptContext
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "090e3ba2a1d93d843715cb8cec50e1730e20991c62b04e7e249ef9b378d1490c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """verify password using plain_password & hashed_password """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """generate hash using plain_password"""
    return pwd_context.hash(password)


def get_user(db, username: str):
    """get users if username in db take 2 arg. 1-db, 2-username"""
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    """authenticate_user using user & password"""
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# This function creates an access token with a given data and expiration time.
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    # Copy the data to a new dictionary to avoid modifying the original data.
    to_encode = data.copy()
    # If an expiration time delta is provided, calculate the expiration time by adding it to the current time.
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    # If no expiration time delta is provided, set the expiration time to 15 minutes from now.
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    # Add the expiration time to the data.
    to_encode.update({"exp": expire})
    # Encode the data into a JWT using the secret key and the specified algorithm.
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # Return the encoded JWT.
    return encoded_jwt

# This asynchronous function retrieves the current user based on the provided token.
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # Define an exception to be raised if the credentials cannot be validated.
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Try to decode the token using the secret key and the specified algorithm.
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extract the username from the payload.
        username: str | None = payload.get("sub")
        # If the username is None, raise the credentials exception.
        if username is None:
            raise credentials_exception
        # Create a TokenData instance with the extracted username.
        token_data = TokenData(username=username)
    # If a JWTError occurs during decoding, raise the credentials exception.
    except JWTError:
        raise credentials_exception
    # If the username in the token data is None, raise the credentials exception.
    if token_data.username is None:
        raise credentials_exception
    # Retrieve the user from the fake users database using the username.
    user = get_user(fake_users_db, username=token_data.username)
    # If the user is None (i.e., the user does not exist), raise the credentials exception.
    if user is None:
        raise credentials_exception
    # If the user exists and the credentials are valid, return the user.
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """check current user active or disabled"""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

