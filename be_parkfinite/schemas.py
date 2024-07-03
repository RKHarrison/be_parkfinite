from pydantic import BaseModel

class CampsiteActivityBase(BaseModel):
    campsite_id: int
    activity_id: int

class CampsiteActivityCreate(CampsiteActivityBase):
    pass

class CampsiteActivity(CampsiteActivityBase):
    campsite_activity_id: int


class ActivityBase(BaseModel):
    activity_name: str
    activity_img_url: str

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    activity_id: int


class CampsiteFacilityBase(BaseModel):
    campsite_id: int
    facility_id: int

class CampsiteFacilityCreate(CampsiteFacilityBase):
    pass

class CampsiteFacility(CampsiteFacilityBase):
    campsite_facility_id: int


class FacilityBase(BaseModel):
    facility_name: str
    facility_img_url: str

class FacilityCreate(FacilityBase):
    pass

class Facility(FacilityBase):
    facility_id: int
   

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

class CampsiteCreate(CampsiteBase):
    # facilities: list[Facilities] | None
    # activities: list[Activities] | None
    contacts: list[CampsiteContact] = []
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
        # orm_mode = True


class CampsiteCategoryBase(BaseModel):
    category_name: str
    category_image_url: str

class CampsiteCategoryCreate(CampsiteCategoryBase):
    pass

class CampsiteCategory(CampsiteCategoryBase):
    category_id: int