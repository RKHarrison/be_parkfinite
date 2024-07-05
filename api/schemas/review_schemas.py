from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: int
    campsite_id: int
    username: str
    comment: str | None = None

class CreateReview(ReviewBase):
    pass

class Review(ReviewBase):
    review_id: int

    class ConfigDict: 
        from_attributes = True
