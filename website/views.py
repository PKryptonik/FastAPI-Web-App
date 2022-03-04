from fastapi import FastAPI

@app.get("/")
def root():
    return {"message": "Hello World"}