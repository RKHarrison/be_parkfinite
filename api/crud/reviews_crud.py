from fastapi import HTTPException
from api.models.review_models import Review
from api.models.campsite_models import Campsite
from api.models.user_models import User
from api.schemas.review_schemas import ReviewCreateRequest, ReviewUpdateRequest
from api.utils.update_campsite_average_rating import update_campsite_average_rating


def create_review_by_campsite_id(db, campsite_id: int, request: ReviewCreateRequest):
    campsite = db.query(Campsite).filter(
        Campsite.campsite_id == campsite_id).first()
    if not campsite:
        raise HTTPException(
            status_code=404, detail="404 - Campsite Not Found!")

    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="404 - User Not Found!")

    new_review = Review(
        campsite_id=campsite_id,
        rating=request.rating,
        comment=request.comment,
        username=request.username
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    update_campsite_average_rating(db, campsite_id, Campsite, Review)
    return new_review


def read_reviews_by_campsite_id(db, id: int):
    reviews = db.query(Review).filter(Review.campsite_id == id).all()
    return reviews


def update_review_by_review_id(db, campsite_id: int, review_id: int, request: ReviewUpdateRequest):
    review = db.get(Review, review_id)
    if not review:
        raise HTTPException(
            status_code=404, detail="404 - Review Not Found!")

    campsite = db.get(Campsite, campsite_id)
    if not campsite:
        raise HTTPException(
            status_code=404, detail="404 - Campsite Not Found!")

    if request.rating:
        review.rating = request.rating
        update_campsite_average_rating(db, campsite_id, Campsite, Review)
        db.commit()
    if request.comment:
        review.comment = request.comment
        db.commit()
    db.refresh(review)
    return review


def remove_review_by_review_id(db, review_id: int):
    review = db.get(Review, review_id)
    if not review:
        raise HTTPException(
            status_code=404, detail="404 - Review Not Found!")
    db.delete(review)
    db.commit()
