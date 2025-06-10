# backend/models/task.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

class Task(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    due: Optional[datetime] = None
    priority: Optional[str] = "normal"  # low, normal, high
