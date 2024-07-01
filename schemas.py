from pydantic import BaseModel

class CampsitePhotoBase(BaseModel):
    campsite_photo_url: str

class CampsitePhotoCreate(CampsitePhotoBase):
    pass

class CampsitePhoto(CampsitePhotoBase):
    campsite_photo_id: int
    campsite_photo_url: str
    campsite_id: int

    class Config:
        orm_mode = True

class CampsiteBase(BaseModel):
    campsite_name: str
    campsite_longitude: float
    campsite_latitude: float

class CampsiteCreate(CampsiteBase):
    pass

class Campsite(CampsiteBase):
    campsite_id: int
    campsite_name: str
    campsite_longitude: float
    campsite_latitude: float
    photos: list[CampsitePhoto] = []

    class Config: 
        orm_mode = True





