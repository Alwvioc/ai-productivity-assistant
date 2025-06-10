# backend/routes/tasks.py
from fastapi import APIRouter, HTTPException
from models.task import Task
from typing import List
from datetime import datetime
import uuid

router = APIRouter()

# In-memory task store (for now)
tasks = []

@router.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    task.id = str(uuid.uuid4())  # Assign a unique ID
    tasks.append(task)
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": "Task deleted"}
