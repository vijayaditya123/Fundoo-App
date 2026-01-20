from pydantic import BaseModel
from datetime import datetime

class LabelCreate(BaseModel):
    user_id: int
    name: str

class LabelResponse(BaseModel):
    label_id: int
    user_id: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True  
