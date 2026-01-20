from datetime import datetime
from pydantic import BaseModel, ConfigDict

class NoteCreate(BaseModel):
    user_id:int
    title: str 
    content: str
    is_archived: bool
    is_deleted : bool
    
class NoteResponse(BaseModel):
    notes_id:int
    user_id:int
    title: str 
    content: str
    is_archived: bool
    is_deleted : bool
    created_at:datetime
    updated_at:datetime
    
    model_config = ConfigDict(from_attributes=True)