from database.database import Base
from typing import List
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column 


class CampsiteCategory(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True)
    category_img_url = Column(String)
    category_name = Column(String)


class Campsite(Base):
    __tablename__ = "campsites"
    campsite_id = Column(Integer, primary_key=True)
    campsite_name = Column(String, index=True)
    campsite_longitude = Column(Float)
    campsite_latitude = Column(Float)
    parking_cost = Column(Float)
    facilities_cost = Column(Float)
    opening_month = Column(String)
    closing_month = Column(String)
    description = Column(String)
    date_added = Column(String)
    added_by = Column(String)
    approved = Column(Boolean, default=False)

    category_id = Column(Integer, ForeignKey("categories.category_id"))
    category = relationship("CampsiteCategory")

    contact: Mapped[List["CampsiteContact"]] = relationship("CampsiteContact", back_populates="campsite")
    photos: Mapped[List["CampsitePhoto"]] = relationship("CampsitePhoto", back_populates="campsite")


class CampsiteContact(Base):
    __tablename__ = "campsite_contacts"
    campsite_contact_id = Column(Integer, primary_key=True)
    campsite_contact_name = Column(String)
    campsite_contact_phone = Column(String)
    campsite_contact_email = Column(String)

    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))
    campsite: Mapped["Campsite"] = relationship("Campsite", back_populates="contact")


class CampsitePhoto(Base):
    __tablename__ = "campsite_photos"
    campsite_photo_id = Column(Integer, primary_key=True)
    campsite_photo_url = Column(String)

    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))
    campsite: Mapped["Campsite"] = relationship("Campsite", back_populates="photos")


