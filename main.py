from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Pages(BaseModel):
    home: str 
    login: str 
    Logout: Optional[str] = "Logout"
   

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}