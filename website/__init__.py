import os

from fastapi import FastAPI
from dotenv import load_dotenv
   

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def create_app():
    app = FastAPI()
    return app
    