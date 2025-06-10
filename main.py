# backend/main.py
from fastapi import FastAPI
from routes import tasks

app = FastAPI()

app.include_router(tasks.router)
@app.get("/")
def root():
    return {"message": "Welcome to the AI Productivity Assistant API"}