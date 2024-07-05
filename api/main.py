from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from os import getenv

from crud.campsite_crud import create_campsite, read_campsites, read_campsite_by_id
from api.crud.reviews_crud import read_reviews_by_campsite_id
from api.crud.user_crud import read_users
from schemas.campsite_schemas import CampsiteCreate, Campsite, CampsiteDetailed
from api.schemas.review_schemas import Review
from api.schemas.user_schemas import User

from database.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/campsites", response_model=list[Campsite])
def get_campsites(skip: int = 0, limit: int = 30, db: Session = Depends(get_db)):
    return read_campsites(db, skip=skip, limit=limit)

@app.get("/campsites/{campsite_id}", response_model=CampsiteDetailed)
def get_campsite_by_campsite_id(campsite_id, db: Session = Depends(get_db)):
    return read_campsite_by_id(db, campsite_id)

@app.get("/campsites/{campsite_id}/reviews", response_model=list[Review])
def get_reviews_by_campsite_id(campsite_id, db: Session = Depends(get_db)):
    reviews = read_reviews_by_campsite_id(db, campsite_id)
    if not reviews:
        raise HTTPException(status_code=404, detail="404 - Reviews Not Found!")
    return reviews


@app.get("/users", response_model=list[User])
def get_users(db: Session = Depends(get_db)):
    return read_users(db)










@app.post("/campsites", response_model=Campsite)
def post_campsite(campsite: CampsiteCreate, db: Session = Depends(get_db)):
    return create_campsite(db=db, campsite=campsite)

if __name__ == "__main__":
    PORT = int(getenv('PORT', 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)