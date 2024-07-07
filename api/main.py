from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import uvicorn
from os import getenv

from crud.campsite_crud import create_campsite, read_campsites, read_campsite_by_id
from api.crud.reviews_crud import read_reviews_by_campsite_id
from api.crud.user_crud import read_users
from schemas.campsite_schemas import CampsiteCreateRequest, Campsite, CampsiteDetailed
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


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    body = exc.body
    if getenv("ENV") == "development":
        print("Validation errors:", errors)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": errors, "body": body}),
    )

@app.exception_handler(AttributeError)
async def attribute_error_handler(request: Request, exc: AttributeError):
    if getenv("ENV") == "development":
        print( f"An attribute error occurred: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "A server error occured"}
    )

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/campsites", status_code=201, response_model=CampsiteDetailed)
def post_campsite(request: CampsiteCreateRequest, db: Session = Depends(get_db)):
    return create_campsite(db=db, request=request)

@app.get("/campsites", response_model=list[Campsite])
def get_campsites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return read_campsites(db, skip=skip, limit=limit)

@app.get("/campsites/{campsite_id}", response_model=CampsiteDetailed)
def get_campsite_by_campsite_id(campsite_id, db: Session = Depends(get_db)):
    return read_campsite_by_id(db, campsite_id)

@app.get("/campsites/{campsite_id}/reviews", response_model=list[Review])
def get_reviews_by_campsite_id(campsite_id, db: Session = Depends(get_db)):
    return read_reviews_by_campsite_id(db, campsite_id)

@app.get("/users", response_model=list[User])
def get_users(db: Session = Depends(get_db)):
    return read_users(db)




if __name__ == "__main__":
    PORT = int(getenv('PORT', 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)