from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: int
    campsite_id: int
    username: str

class CreateReview(ReviewBase):
    comment: str | None = None

class Review(ReviewBase):
    review_id: str