from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from src.db.base import Base

class Label(Base):
    __tablename__ = "labels"

    label_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
