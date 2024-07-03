from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base

class CampsiteCategory(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True)
    category_image_url = Column(String)
    category_name = Column(String)

class Campsite(Base):
    __tablename__ = "campsites"

    campsite_id = Column(Integer, primary_key=True)
    campsite_name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    campsite_longitude = Column(Float)
    campsite_latitude = Column(Float)
    parking_cost = Column(Float)
    facilities_cost = Column(Float)
    # average_rating = Column(Float)
    opening_month = Column(String)
    closing_month = Column(String)
    description = Column(String)
    date_added = Column(String)
    added_by = Column(String)

    campsite_photos = relationship("CampsitePhoto", back_populates="photos")
    campsite_contacts = relationship("CampsiteContact", back_populates="contacts")

class CampsitePhoto(Base):
    __tablename__ = "campsite_photos"

    campsite_photo_id = Column(Integer, primary_key=True)
    campsite_photo_url = Column(String)
    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))

    photos = relationship("Campsite", back_populates="campsite_photos")

class CampsiteContact(Base):
    __tablename__ = "campsite_contacts"

    campsite_contact_id = Column(Integer, primary_key=True)
    campsite_contact_name = Column(String)
    campsite_contact_phone = Column(String)
    campsite_contact_email = Column(String)
    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))

    contacts = relationship("Campsite", back_populates="campsite_contacts")

class Facility(Base):
    __tablename__ = "facilities"

    facility_id = Column(Integer, primary_key=True)
    facility_name = Column(String)
    facility_img_url = Column(String)

class CampsiteFacility(Base):
    __tablename__ = 'campsite_facilities'

    campsite_facility_id = Column(Integer, primary_key=True)
    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))
    facility_id = Column(Integer, ForeignKey("facilities.facility_id"))

class Activity(Base):
    __tablename__ = "activities"

    activity_id = Column(Integer,primary_key=True)
    activity_name = Column(String)
    activity_img_url = Column(String)

class CampsiteActivity(Base):
    __tablename__ = 'campsite_activities'

    campsite_activity_id = Column(Integer, primary_key=True)
    campsite_id = Column(Integer, ForeignKey("campsites.campsite_id"))
    activity_id = Column(Integer, ForeignKey("activities.activity_id"))



