from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models, be_parkfinite.crud.campsite_crud as campsite_crud, be_parkfinite.schemas.campsite_schemas as campsite_schemas
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


@app.get("/campsites", response_model=list[campsite_schemas.Campsite])
def read_campsites(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    campsites = campsite_crud.get_campsites(db, skip=skip, limit=limit)
    return campsites

@app.post("/campsites", response_model=campsite_schemas.Campsite)
def create_campsite(campsite: campsite_schemas.CampsiteCreate, db: Session = Depends(get_db)):
    return campsite_crud.create_campsite(db=db, campsite=campsite)