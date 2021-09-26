from typing import Optional
from datetime import date, time, timedelta

from pydantic import BaseModel


# Shared properties
class TaskBase(BaseModel):
    title: str
    task_date: date
    start_time: time
    end_time: time
    duration: float


# Properties to receive on task creation
class TaskCreate(TaskBase):
    title: str


# Properties to receive on task update
class TaskUpdate(TaskBase):
    pass


# Properties shared by models stored in DB
class TaskInDBBase(TaskBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Task(TaskInDBBase):
    pass


# Properties properties stored in DB
class TaskInDB(TaskInDBBase):
    pass
