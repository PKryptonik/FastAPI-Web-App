from typing import List, Optional

from pydantic import BaseModel

class NoteBase(BaseModel):
    description: str

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    notes: List[Note] = []

    class Config:
        orm_mode = True