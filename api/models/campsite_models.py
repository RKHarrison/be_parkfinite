from typing import List
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from database.database import Base
from api.utils.date_stamp import date_stamp


class CampsiteCategory(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True)
    category_img_url = Column(String)
    category_name = Column(String)


campsites_facilities = Table(
    "campsites_facilities",
    Base.metadata,
    Column("campsite_id", ForeignKey("campsites.campsite_id", ondelete="CASCADE"), primary_key=True),
    Column("facility_id", ForeignKey("facilities.facility_id", ondelete="CASCADE"), primary_key=True),
)


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
    date_added = Column(String, default=date_stamp())
    added_by = Column(String, ForeignKey("users.username"))
    approved = Column(Boolean, default=False)

    category_id = Column(Integer, ForeignKey("categories.category_id"))
    category = relationship("CampsiteCategory")

    contacts: Mapped[List["CampsiteContact"]] = relationship("CampsiteContact", back_populates="campsite", cascade="all, delete-orphan")
    photos: Mapped[List["CampsitePhoto"]] = relationship("CampsitePhoto", back_populates="campsite", cascade="all, delete-orphan")
    # facilities: Mapped[List["Facility"]] = relationship(secondary=campsites_facilities, cascade="all, delete-orphan")

class CampsiteContact(Base):
    __tablename__ = "campsite_contacts"
    campsite_contact_id = Column(Integer, primary_key=True)
    campsite_contact_name = Column(String)
    campsite_contact_phone = Column(String)
    campsite_contact_email = Column(String)

    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))
    campsite: Mapped["Campsite"] = relationship("Campsite", back_populates="contacts")


class CampsitePhoto(Base):
    __tablename__ = "campsite_photos"
    campsite_photo_id = Column(Integer, primary_key=True)
    campsite_photo_url = Column(String)

    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))
    campsite: Mapped["Campsite"] = relationship("Campsite", back_populates="photos")


