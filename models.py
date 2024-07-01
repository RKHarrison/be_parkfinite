from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Campsite(Base):
    __tablename__ = "campsites"

    campsite_id = Column(Integer, primary_key=True)
    campsite_name = Column(String, index=True)
    campsite_longitude = Column(Float)
    campsite_latitude = Column(Float)

    campsite_photos = relationship("CampsitePhoto", back_populates="photos")

class CampsitePhoto(Base):
    __tablename__ = "campsite_photos"

    campsite_photo_id = Column(Integer, primary_key=True)
    campsite_photo_url = Column(String)
    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))

