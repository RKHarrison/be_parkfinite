from sqlalchemy import Column, Integer, String, ForeignKey

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