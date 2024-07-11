from fastapi import HTTPException
from api.models.campsite_models import Campsite, CampsitePhoto, CampsiteContact, CampsiteCategory
from api.models.review_models import Review
from schemas.campsite_schemas import CampsiteCreateRequest
from utils.update_campsite_average_rating import update_campsite_average_rating


def create_campsite(db, request: CampsiteCreateRequest):

    category = db.query(CampsiteCategory).filter(
        CampsiteCategory.category_id == request.category_id).first()
    if not category:
        raise HTTPException(
            status_code=422, detail="Category ID does not exist!")

    new_campsite = Campsite(
        campsite_name=request.campsite_name,
        campsite_longitude=request.campsite_longitude,
        campsite_latitude=request.campsite_latitude,
        parking_cost=request.parking_cost,
        facilities_cost=request.facilities_cost,
        added_by=request.added_by,
        category_id=request.category_id,
        opening_month=request.opening_month,
        closing_month=request.closing_month
    )
    db.add(new_campsite)
    db.commit()
    db.refresh(new_campsite)

    for photo_request in request.photos:
        new_photo = CampsitePhoto(
            campsite_photo_url=photo_request.campsite_photo_url,
            campsite_id=new_campsite.campsite_id
        )
        db.add(new_photo)
    db.commit()

    for contact_request in request.contacts:
        new_contact = CampsiteContact(
            campsite_contact_name=contact_request.campsite_contact_name,
            campsite_contact_phone=contact_request.campsite_contact_phone,
            campsite_contact_email=contact_request.campsite_contact_email,
            campsite_id=new_campsite.campsite_id
        )
        db.add(new_contact)
    db.commit()

    return new_campsite


def read_campsites(db, skip: int = 0, limit: int = 250):
    campsites = db.query(Campsite).limit(limit).all()
    for campsite in campsites:
        update_campsite_average_rating(
            db, campsite.campsite_id, Campsite, Review)

    return campsites


def read_campsite_by_id(db, id: int):
    campsite = db.get(Campsite, id)
    if not campsite:
        raise HTTPException(
            status_code=404, detail="404 - Campsite Not Found!")
    update_campsite_average_rating(db, campsite.campsite_id, Campsite, Review)
    return campsite
