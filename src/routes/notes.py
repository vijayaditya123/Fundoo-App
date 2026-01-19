from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from src.db.session import SessionLocal
from src.modules.notes import  Note
from src.schemas.notes import NoteCreate,NoteResponse

router = APIRouter(prefix="/notes")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",response_model=NoteResponse) 
def  create_note(note:NoteCreate,db: Session = Depends(get_db)):
    db_note = Note(
          user_id = note.user_id,
          title= note.title,
          content=note.content,
          is_archived= note.is_archived,
          is_deleted = note.is_deleted
       )
    db.add( db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("/",response_model=list[NoteResponse])
def get_all_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()

@router.get("/{notes_id}",response_model = NoteResponse)
def get_notes(notes_id:int,db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.notes_id==notes_id).first()
    if not note :
        raise HTTPException(status_code=404, detail="Note not found")
    
    return note

@router.put("/{notes_id}",response_model = NoteResponse)
def update_notes(notes_id:int,note_data:NoteCreate,db: Session = Depends(get_db)):
    note= db.query(Note).filter(Note.notes_id == notes_id).first()
    if not note :
        raise HTTPException(status_code=404, detail="Note not found")
    note.user_id=note_data.user_id
    note.title=note_data.title
    note.content= note_data.content
    note.is_archived=note_data.is_archived
    note.is_deleted =note_data.is_deleted
    
    db.commit()
    db.refresh(note)
    return note

@router.delete("/{notes_id}",response_model = NoteResponse)
def delete_notes(notes_id:int,db: Session = Depends(get_db)):
    note= db.query(Note).filter(Note.notes_id == notes_id).first()
    if not note :
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    return note




