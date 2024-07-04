from database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    user_password = Column(String)
    user_firstname = Column(String)
    user_lastname = Column(String)
    user_email = Column(String)
    xp = Column(Integer, default=0)
    user_type = Column(String, default="NORMAL")
    camera_permission = Column(Boolean, default=False)

class UserCampsite(Base):
    __tablename__ = "user_campsites"

    user_campsite_id = Column(Integer, primary_key=True)
    username = Column(String, ForeignKey("users.username"))
    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))
