from fastapi import HTTPException
from api.models.review_models import Review
from api.schemas.review_schemas import ReviewCreateRequest


def read_reviews_by_campsite_id(db, id: int):
    reviews = db.query(Review).filter(Review.campsite_id == id).all()
    if not reviews:
        raise HTTPException(status_code=404, detail="404 - Reviews Not Found!")
    return reviews


def create_review_by_campsite_id(db, campsite_id: int, request: ReviewCreateRequest):
    new_review = Review(
        campsite_id=campsite_id,
        rating=request.rating,
        comment=request.comment,
        username=request.username
    )
    print(new_review)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    print(new_review)
    return new_review
