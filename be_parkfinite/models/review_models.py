from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    campiste_id = Column(Integer,ForeignKey("campsites.campsite_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))