from pydantic import BaseModel

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
   