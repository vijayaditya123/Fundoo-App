from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.session import SessionLocal
from src.modules.label import Label
from src.schemas.label import LabelCreate, LabelResponse

router = APIRouter(prefix="/labels")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=LabelResponse)
def create_label(label: LabelCreate, db: Session = Depends(get_db)):
    db_label = Label(
        user_id=label.user_id,
        name=label.name
    )
    db.add(db_label)
    db.commit()
    db.refresh(db_label)
    return db_label

@router.get("/", response_model=list[LabelResponse])
def get_all_labels(db: Session = Depends(get_db)):
    return db.query(Label).all()

@router.get("/{label_id}", response_model=LabelResponse)
def get_label(label_id: int, db: Session = Depends(get_db)):
    label = db.query(Label).filter(Label.label_id == label_id).first()
    if not label:
        raise HTTPException(status_code=404, detail="Label not found")
    return label

@router.delete("/{label_id}")
def delete_label(label_id: int, db: Session = Depends(get_db)):
    label = db.query(Label).filter(Label.label_id == label_id).first()
    if not label:
        raise HTTPException(status_code=404, detail="Label not found")
    db.delete(label)
    db.commit()
    return {"message": "Label deleted successfully"}
