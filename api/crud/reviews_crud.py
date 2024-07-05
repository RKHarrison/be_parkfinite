from fastapi import HTTPException
from api.models.review_models import Review

def read_reviews_by_campsite_id(db, id: int):
    reviews = db.query(Review).filter(Review.campsite_id == id).all()
    if not reviews:
        raise HTTPException(status_code=404, detail="404 - Reviews Not Found!")
    return reviews