from sqlalchemy import Column, Integer, String, ForeignKey

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



