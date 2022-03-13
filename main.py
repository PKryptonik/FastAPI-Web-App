from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header
from routers import users, notes

app = FastAPI()

app.include_router(notes.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Activation."}