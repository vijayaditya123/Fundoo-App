from sqlalchemy import Column,Integer,String,Boolean,DateTime,Text, ForeignKey;
from src.db.base import Base
from datetime import datetime
class Note(Base):
    __tablename__="notes"
    notes_id =Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("users.user_id"), nullable=False)
    title = Column(String(100))
    content = Column(Text)
    is_archived=Column(Boolean,default=False)
    is_deleted=Column(Boolean,default=False)
    created_at=Column(DateTime,default=datetime.utcnow)
    updated_at=Column(DateTime,default=datetime.utcnow)
    
    
