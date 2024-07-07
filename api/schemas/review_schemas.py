from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: int
    username: str
    comment: str | None = None

class ReviewCreateRequest(ReviewBase):
    pass

class Review(ReviewBase):
    review_id: int
    campsite_id: int

    class ConfigDict: 
        from_attributes = True
