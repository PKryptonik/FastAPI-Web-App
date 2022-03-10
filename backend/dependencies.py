import os

from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def get_token_header(x_token: str = Header(...)):
    if x_token != SECRET_KEY:
        raise HTTPException(status_code=400, detail="X-Token header invalid")

def get_query_token(token: str):
    if token != "example":
        raise HTTPException(status_code=400, detail="no token provided")