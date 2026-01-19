from sqlalchemy import Column,Integer,String,Boolean,DateTime
from src.db.base import Base
from datetime import datetime  

class User(Base):
    __tablename__="users"
    
    user_id =Column(Integer,primary_key = True,index=True)
    full_name = Column(String(100),nullable=False)
    email= Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
    is_active= Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.utcnow)
    updated_at = Column(DateTime,default=datetime.utcnow)

    

    