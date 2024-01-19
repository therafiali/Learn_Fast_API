from data import fake_users_db
from models import UserInDB

def get_user(db, username: str):
    """get users if username in db take 2 arg. 1-db, 2-username"""
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)



def fake_decode_token(token):
    """in this func use get_user() func, 1-db = fake_users_db, 2-username = token"""
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user



def find_user_dict(username: str):
    """find user in db take 1 arg. 1-username"""
    return fake_users_db.get(username)