from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    username = Column(String, ForeignKey("users.username"))

    campsite_id = Column(Integer, ForeignKey(
        "campsites.campsite_id", ondelete="CASCADE"))
    campsite = relationship("Campsite", back_populates="reviews")
