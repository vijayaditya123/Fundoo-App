from pydantic import BaseModel
from datetime import datetime
class UserCreate(BaseModel):
    full_name:str
    email:str
    password: str


class UserResponse(BaseModel):
    user_id:int
    full_name:str
    email:str
    is_active:bool
    created_at:datetime
    updated_at:datetime
    class Config:
      orm_mode = True


 