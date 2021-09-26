from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.task import TaskCreate
from tests.utils.utils import random_lower_string


def create_random_task(db: Session) -> models.Task:
    title = random_lower_string()
    task_date = "2021-10-10"
    start_time = "09:00"
    end_time = "10:00"
    duration = 3600
    task_in = TaskCreate(title=title, task_date=task_date, start_time=start_time, end_time=end_time, duration=duration, id=id)
    return crud.task.create(db=db, obj_in=task_in)
