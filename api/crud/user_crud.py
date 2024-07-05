from api.models.user_models import User


def read_users(db):
    users = db.query(User).all()
    return users