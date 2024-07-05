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


class CampsiteContactBase(BaseModel):
    campsite_contact_name: str
    campsite_contact_phone: str
    

class CampsiteContactCreate(CampsiteContactBase):
    campsite_contact_email: str | None = None

class CampsiteContact(CampsiteContactBase):
    campsite_contact_email: str | None = None
    campsite_contact_id: int
    campsite_id: int

    class ConfigDict: 
        from_attributes = True


class CampsiteCategoryBase(BaseModel):
    category_name: str
    category_img_url: str

class CampsiteCategoryCreate(CampsiteCategoryBase):
    pass

class CampsiteCategory(CampsiteCategoryBase):
    pass


class CampsiteBase(BaseModel):
    campsite_name: str
    campsite_id: int
    date_added: str
    added_by: str
    campsite_longitude: float
    campsite_latitude: float
    category: CampsiteCategory
    photos: list[CampsitePhoto] = []
    contact: list[CampsiteContact] = []
    parking_cost: float | None = None
    facilities_cost: float | None = None
    description: str

class CampsiteCreate(CampsiteBase):
    facilities: list[Facility] | None = None
    activities: list[Activity] | None = None
    opening_month: str | None = None
    closing_month: str | None = None

class Campsite(CampsiteBase):
    campsite_id: int
    approved: bool = False

    class ConfigDict: 
        from_attributes = True

class CampsiteDetailed(CampsiteBase):
    campsite_id: int
    approved: bool = False
    facilities: list[Facility] | None = None
    activities: list[Activity] | None = None
    opening_month: str | None = None
    closing_month: str | None = None

    class ConfigDict: 
        from_attributes = True
