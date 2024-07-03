#Create, Read, Update & Delete
from sqlalchemy.orm import Session

from be_parkfinite.models.campsite_models import Campsite
from be_parkfinite.schemas.campsite_schemas import CampsiteCreate

def get_campsites(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Campsite).limit(limit).all()

def create_campsite(db: Session, campsite: CampsiteCreate):
    db_campsite = Campsite(
        # campsite_id = campsite.campsite_id,
        campsite_name = campsite.campsite_name,
        campsite_longitude = campsite.campsite_longitude,
        campsite_latitude = campsite.campsite_longitude
    )
    db.add(db_campsite)
    db.commit()
    db.refresh(db_campsite)
    return db_campsite