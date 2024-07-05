from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from os import getenv

from crud.campsite_crud import fetch_campsites, insert_campsite
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
def get_campsites(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return fetch_campsites(db, skip=skip, limit=limit)











@app.post("/campsites", response_model=Campsite)
def post_campsite(campsite: CampsiteCreate, db: Session = Depends(get_db)):
    return insert_campsite(db=db, campsite=campsite)

if __name__ == "__main__":
    PORT = int(getenv('PORT', 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)