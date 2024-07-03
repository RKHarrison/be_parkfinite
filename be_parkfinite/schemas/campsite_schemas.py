from pydantic import BaseModel
from schemas.facility_schemas import Facility
from schemas.activity_schemas import Activity

class CampsitePhotoBase(BaseModel):
    campsite_photo_url: str

class CampsitePhotoCreate(CampsitePhotoBase):
    pass

class CampsitePhoto(CampsitePhotoBase):
    campsite_photo_id: int
    campsite_id: int

    class ConfigDict:
        from_attributes = True
        # orm_mode = True


class CampsiteContactBase(BaseModel):
    campsite_contact_name: str
    campsite_contact_phone: str

class CampsiteContactCreate(CampsiteContactBase):
    campsite_contact_email: str

class CampsiteContact(CampsiteContactBase):
    campsite_contact_id: int
    campsite_id: int

    class ConfigDict: 
        from_attributes = True
        # orm_mode = True

class CampsiteBase(BaseModel):
    campsite_name: str
    campsite_longitude: float
    campsite_latitude: float
    parking_cost: float
    facilities_cost: float
    description: str
    approved: bool = False

class CampsiteCreate(CampsiteBase):
    facilities: list[Facility] | None = None
    activities: list[Activity] | None = None
    contacts: list[CampsiteContact] | None = None
    opening_month: str
    closing_month: str

class Campsite(CampsiteBase):
    campsite_id: int
    category_id: int
    photos: list[CampsitePhoto] = []
    date_added: str
    added_by: str

    class ConfigDict: 
        from_attributes = True


class CampsiteCategoryBase(BaseModel):
    category_name: str
    category_image_url: str

class CampsiteCategoryCreate(CampsiteCategoryBase):
    pass

class CampsiteCategory(CampsiteCategoryBase):
    category_id: int