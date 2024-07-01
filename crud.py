#Create, Read, Update & Delete
from sqlalchemy.orm import Session

import models, schemas

def get_campsites(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Campsite).limit(limit).all()

def create_campsite(db: Session, campsite: schemas.CampsiteCreate):
    db_campsite = models.Campsite(
        # campsite_id = campsite.campsite_id,
        campsite_name = campsite.campsite_name,
        campsite_longitude = campsite.campsite_longitude,
        campsite_latitude = campsite.campsite_longitude
    )
    db.add(db_campsite)
    db.commit()
    db.refresh(db_campsite)
    return db_campsite