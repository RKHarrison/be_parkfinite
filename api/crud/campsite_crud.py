#Create, Read, Update & Delete
from sqlalchemy.orm import Session, joinedload, selectinload

from api.models.campsite_models import Campsite
from schemas.campsite_schemas import CampsiteCreate

def fetch_campsites(db: Session, skip: int = 0, limit: int = 10):
    campsites = db.query(Campsite).limit(limit).all()
    return campsites





def insert_campsite(db: Session, campsite: CampsiteCreate):
    db_campsite = Campsite(
        campsite_name = campsite.campsite_name,
        campsite_longitude = campsite.campsite_longitude,
        campsite_latitude = campsite.campsite_longitude
    )
    db.add(db_campsite)
    db.commit()
    db.refresh(db_campsite)
    return db_campsite