from fastapi import HTTPException
from api.models.campsite_models import Campsite, CampsitePhoto
from schemas.campsite_schemas import CampsiteCreateRequest

def create_campsite(db, request: CampsiteCreateRequest):
    new_campsite = Campsite(
        campsite_name = request.campsite_name,
        campsite_longitude = request.campsite_longitude,
        campsite_latitude = request.campsite_latitude,
        parking_cost = request.parking_cost,
        facilities_cost = request.facilities_cost,
        added_by = request.added_by,
        category_id = request.category_id,
        opening_month = request.opening_month,
        closing_month = request.closing_month
    )
    db.add(new_campsite)
    db.commit()
    db.refresh(new_campsite)

    for photo in request.photos:
        db_photo = CampsitePhoto(
            campsite_photo_url=photo.campsite_photo_url,
            campsite_id=new_campsite.campsite_id
        )
        db.add(db_photo)
    db.commit()
    return new_campsite

def read_campsites(db, skip: int = 0, limit: int = 30):
    campsites = db.query(Campsite).limit(limit).all()
    return campsites

def read_campsite_by_id(db, id: int):
    campsite = db.get(Campsite, id)
    if not campsite:
        raise HTTPException(status_code=404, detail="404 - Campsite Not Found!")
    return campsite