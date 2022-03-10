from fastapi import Depends, FastAPI

from backend.dependencies import get_query_token, get_token_header
from backend.routers import users, notes

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(notes.router)
app.include_router(
    users.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "The machine is experiencing uncertainty."}},
)

@app.get("/")
def root():
    return {"message": "Activation."}