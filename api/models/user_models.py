from typing import List
from database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped

user_campsite_favourites = Table(
    "user_campsite_favourites",
    Base.metadata,
    Column("username", String, ForeignKey('users.username', ondelete="CASCADE"), primary_key=True),
    Column("campsite_id", Integer, ForeignKey("campsites.campsite_id", ondelete="CASCADE"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    username = Column(String(30), primary_key=True)
    user_password = Column(String)
    user_firstname = Column(String)
    user_lastname = Column(String)
    user_email = Column(String)
    xp = Column(Integer, default=0)
    user_type = Column(String, default="NORMAL")
    camera_permission = Column(Boolean, default=False)
    favourites: Mapped[List["Campsite"]] = relationship('Campsite', secondary=user_campsite_favourites, back_populates='favourited_by')
