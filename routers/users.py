from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    user_id: int
    user_name: str

@router.get("/user")
def root():
    return {"message": "this should pull up users"}