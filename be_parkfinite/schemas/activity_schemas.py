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
