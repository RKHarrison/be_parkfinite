from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud.campsite_crud import get_campsites, create_campsite
from schemas.campsite_schemas import Campsite, CampsiteCreate
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
def read_campsites(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    campsites = get_campsites(db, skip=skip, limit=limit)
    return campsites

@app.post("/campsites", response_model=Campsite)
def create_campsite(campsite: CampsiteCreate, db: Session = Depends(get_db)):
    return create_campsite(db=db, campsite=campsite)