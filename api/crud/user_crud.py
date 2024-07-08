from fastapi import HTTPException
from api.models.user_models import User, user_campsite_favourites
from api.models.campsite_models import Campsite



def read_users(db):
    users = db.query(User).all()
    return users

def read_user_by_username(db, username):
    user = db.get(User, username)
    if not user:
        raise HTTPException(status_code=404, detail="404 - User Not Found!")
    return user

def read_user_campsite_favourites_by_username(db, username: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="404 - User Not Found!")
    print(user.username)
    return user.favourites
