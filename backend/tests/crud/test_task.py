from sqlalchemy.orm import Session
from datetime import datetime

from app import crud
from app.schemas.task import TaskCreate, TaskUpdate
from tests.utils.utils import random_lower_string


def test_create_task(db: Session) -> None:
    title = random_lower_string()
    task_date = "2021-10-10"
    start_time = "09:00"
    end_time = "10:00"
    duration = 3600
    task_in = TaskCreate(title=title, task_date=task_date, start_time=start_time, end_time=end_time, duration=duration)
    task = crud.task.create(db=db, obj_in=task_in)
    assert task.title == title
    assert task.task_date.strftime("%Y-%m-%d") == task_date
    assert task.start_time.strftime("%H:%M") == start_time
    assert task.end_time.strftime("%H:%M") == end_time
    assert task.duration == duration


def test_get_task(db: Session) -> None:
    title = random_lower_string()
    task_date = "2021-10-09"
    start_time = "09:00"
    end_time = "10:00"
    duration = 3600
    task_in = TaskCreate(title=title, task_date=task_date, start_time=start_time, end_time=end_time, duration=duration)
    task = crud.task.create(db=db, obj_in=task_in)
    stored_task = crud.task.get(db=db, id=task.id)
    assert stored_task
    assert task.id == stored_task.id
    assert task.title == title
    assert task.task_date.strftime("%Y-%m-%d") == task_date
    assert task.start_time.strftime("%H:%M") == start_time
    assert task.end_time.strftime("%H:%M") == end_time
    assert task.duration == duration


def test_update_task(db: Session) -> None:
    title = random_lower_string()
    task_date = "2021-10-10"
    start_time = "09:00"
    end_time = "10:00"
    duration = 3600
    task_in = TaskCreate(title=title, task_date=task_date, start_time=start_time, end_time=end_time, duration=duration)
    task = crud.task.create(db=db, obj_in=task_in)
    task_date2 = "2021-10-11"
    task_update = TaskUpdate(title=title, task_date=task_date2, start_time=start_time, end_time=end_time, duration=duration)
    task2 = crud.task.update(db=db, db_obj=task, obj_in=task_update)
    assert task.id == task2.id
    assert task.title == task2.title
    assert task2.task_date.strftime("%Y-%m-%d") == task_date2
    assert task.start_time == task2.start_time
    assert task.end_time == task2.end_time
    assert task.duration == task2.duration


def test_delete_task(db: Session) -> None:
    title = random_lower_string()
    task_date = "2021-10-10"
    start_time = "09:00"
    end_time = "10:00"
    duration = 3600
    task_in = TaskCreate(title=title, task_date=task_date, start_time=start_time, end_time=end_time, duration=duration)
    task = crud.task.create(db=db, obj_in=task_in)
    task2 = crud.task.remove(db=db, id=task.id)
    task3 = crud.task.get(db=db, id=task.id)
    assert task3 is None
    assert task2.id == task.id
    assert task2.title == title
    assert task2.task_date.strftime("%Y-%m-%d") == task_date
    assert task2.start_time.strftime("%H:%M") == start_time
    assert task2.end_time.strftime("%H:%M") == end_time
    assert task2.duration == duration
