from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models, crud, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

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


@app.get("/campsites", response_model=list[schemas.Campsite])
def read_campsites(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    campsites = crud.get_campsites(db, skip=skip, limit=limit)
    return campsites

@app.post("/campsites", response_model=schemas.Campsite)
def create_campsite(campsite: schemas.CampsiteCreate, db: Session = Depends(get_db)):
    return crud.create_campsite(db=db, campsite=campsite)