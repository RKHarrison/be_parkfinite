from pydantic import BaseModel
from api.schemas.facility_schemas import Facility
from api.schemas.activity_schemas import Activity
from api.utils.date_stamp import date_stamp


class CampsitePhotoBase(BaseModel):
    campsite_photo_url: str


class CampsitePhotoCreateRequest(CampsitePhotoBase):
    pass


class CampsitePhoto(CampsitePhotoBase):
    campsite_photo_id: int
    campsite_id: int

    class ConfigDict:
        from_attributes = True


class CampsiteContactBase(BaseModel):
    campsite_contact_name: str
    campsite_contact_phone: str
    campsite_contact_email: str | None = None


class CampsiteContactCreateRequest(CampsiteContactBase):
    pass


class CampsiteContact(CampsiteContactBase):
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
    category_id: int


class CampsiteBase(BaseModel):
    campsite_name: str
    campsite_longitude: float
    campsite_latitude: float
    contacts: list[CampsiteContact] = []
    parking_cost: float | None = None
    facilities_cost: float | None = None
    description: str | None = None
    opening_month: str | None = None
    closing_month: str | None = None


class CampsiteCreateRequest(CampsiteBase):
    photos: list[CampsitePhotoCreateRequest] | None = []
    added_by: str
    category_id: int
    contacts: list[CampsiteContactCreateRequest] | None = []
    facilities: list[Facility] | None = None
    activities: list[Activity] | None = None


class Campsite(CampsiteBase):
    photos: list[CampsitePhoto]
    added_by: str
    campsite_id: int
    category: CampsiteCategory | None = None
    date_added: str | None = None
    approved: bool = False
    average_rating: float | None = None

    class ConfigDict:
        from_attributes = True


class CampsiteDetailed(CampsiteBase):
    photos: list[CampsitePhoto]
    added_by: str
    campsite_id: int
    category_id: int
    category: CampsiteCategory | None = None
    date_added: str
    approved: bool = False
    facilities: list[Facility] | None = None
    activities: list[Activity] | None = None
    average_rating: float | None = None

    class ConfigDict:
        from_attributes = True
