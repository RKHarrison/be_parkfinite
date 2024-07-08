from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from api.models.campsite_models import Campsite


class Facility(Base):
    __tablename__ = "facilities"

    facility_id = Column(Integer, primary_key=True)
    facility_name = Column(String)
    facility_img_url = Column(String)
