import uvicorn
from os import getenv
from fastapi import FastAPI, Depends
from fastapi.exceptions import RequestValidationError, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base
from api.crud.campsite_crud import create_campsite, read_campsites, read_campsite_by_id
from api.crud.reviews_crud import create_review_by_campsite_id, read_reviews_by_campsite_id
from api.crud.user_crud import read_users, read_user_by_username, update_user_xp, create_user_favourite_campsite, read_user_campsite_favourites_by_username, remove_user_favourite_campsite
from api.schemas.campsite_schemas import CampsiteCreateRequest, Campsite, CampsiteDetailed
from api.schemas.review_schemas import Review, ReviewCreateRequest
from api.schemas.user_schemas import User
from api.errors.error_handling import (
    validation_exception_handler, attribute_error_handler,  http_exception_handler, sqlalchemy_exception_handler)

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(AttributeError, attribute_error_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)


@app.get("/")
def health_check():
    return {"Server": "Healthy and happy!"}


@app.post("/campsites", status_code=201, response_model=CampsiteDetailed)
def post_campsite(request: CampsiteCreateRequest, db: Session = Depends(get_db)):
    return create_campsite(db=db, request=request)


@app.get("/campsites", response_model=list[Campsite])
def get_campsites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return read_campsites(db, skip=skip, limit=limit)


@app.get("/campsites/{campsite_id}", response_model=CampsiteDetailed)
def get_campsite_by_campsite_id(campsite_id, db: Session = Depends(get_db)):
    return read_campsite_by_id(db, campsite_id)


@app.post("/campsites/{campsite_id}/reviews", status_code=201, response_model=Review)
def post_review_by_campsite_id(campsite_id, request: ReviewCreateRequest, db: Session = Depends(get_db)):
    return create_review_by_campsite_id(db=db, campsite_id=campsite_id, request=request)


@app.get("/campsites/{campsite_id}/reviews", response_model=list[Review])
def get_reviews_by_campsite_id(campsite_id, db: Session = Depends(get_db)):
    return read_reviews_by_campsite_id(db, campsite_id)


@app.get("/users", response_model=list[User])
def get_users(db: Session = Depends(get_db)):
    return read_users(db)


@app.get("/users/{username}", response_model=User)
def get_user_by_id(username, db: Session = Depends(get_db)):
    return read_user_by_username(db, username)

@app.patch("/users/{username}/{xp}", response_model=User)
def patch_user_xp(username: str, xp: str, db: Session = Depends(get_db)):
    return update_user_xp(db=db, username=username, xp=xp)



@app.get("/users/{username}/favourites", response_model=list[Campsite])
def get_user_favourite_campsites(username, db: Session = Depends(get_db)):
    favourites = read_user_campsite_favourites_by_username(db, username)
    print(favourites)
    return favourites


@app.post("/users/{username}/favourites/{campsite_id}", status_code=201)
def post_user_favourite_campsite(username, campsite_id, db: Session = Depends(get_db)):
    return create_user_favourite_campsite(db=db, username=username, campsite_id=campsite_id)


@app.delete("/users/{username}/favourites/{campsite_id}", status_code=204)
def delete_user_favourite_campsite(username, campsite_id, db: Session = Depends(get_db)):
    return remove_user_favourite_campsite(db=db, username=username, campsite_id=campsite_id, )


if __name__ == "__main__":
    PORT = int(getenv('PORT', 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
