from fastapi import APIRouter

router = APIRouter()

@router.get("/notes")
def root():
    return {"message": "this should pull up notes"}