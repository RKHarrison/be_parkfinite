from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    user_password: str
    user_firstname: str
    user_lastname: str
    user_email: str
    xp: int
    user_type: str
    camera_permission: bool

class CreateUser(UserBase):
    pass    

class User(UserBase):
    pass



class UserCampsiteBase(BaseModel):
    username: str
    campsite_id: int

class CreateUserCampsite(UserCampsiteBase):
    pass

class UserCampsite(UserCampsiteBase):
    user_campsite_id: int