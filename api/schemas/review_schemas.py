from pydantic import BaseModel, Field, field_validator
from typing import Annotated


class ReviewBase(BaseModel):
    rating: Annotated[int, Field(ge=1, le=5)]
    username: str
    comment: Annotated[str, Field(max_length=350)] | None = ""

    @field_validator('rating')
    def validate_rating(cls, rating):
        if rating < 1 or rating > 5:
            raise ValueError('Rating should be between 1 and 5')
        return rating

    @field_validator('comment')
    def validate_comment(cls, comment):
        if comment is not None and len(comment) > 350:
            raise ValueError('String should have at most 350 characters')
        return comment


class ReviewCreateRequest(ReviewBase):
    pass


class Review(ReviewBase):
    review_id: int
    campsite_id: int

    class ConfigDict:
        from_attributes = True
