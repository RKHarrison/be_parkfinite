from fastapi import HTTPException
from api.models.user_models import User


def read_users(db):
    users = db.query(User).all()
    return users

def read_user_by_username(db, username):
    user = db.get(User, username)
    if not user:
        raise HTTPException(status_code=404, detail="404 - User Not Found!")
    return user