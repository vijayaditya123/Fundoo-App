from fastapi import FastAPI

from src.routes.users import router as user_router
from src.routes.notes import router as note_router
from src.routes.label import router as label_router

app = FastAPI()

app.include_router(user_router)
app.include_router(note_router)
app.include_router(label_router)


