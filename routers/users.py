from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    user_id: int
    user_name: str

@router.get("/users")
def root():
    return {"data": User}