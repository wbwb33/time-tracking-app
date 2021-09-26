from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Task])
def read_tasks(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve tasks.
    """
    tasks = crud.task.get_multi(
        db=db, skip=skip, limit=limit
    )
    return tasks

@router.get("/date/{task_date}", response_model=List[schemas.Task])
def read_tasks_filtered_by_date(
    *,
    db: Session = Depends(deps.get_db),
    task_date: str,
) -> Any:
    """
    Retrieve tasks filtered by date.
    """
    tasks = crud.task.get_with_date_as_filter(
        db=db, task_date=task_date
    )
    return tasks


@router.post("/", response_model=schemas.Task)
def create_task(
    *,
    db: Session = Depends(deps.get_db),
    task_in: schemas.TaskCreate,
) -> Any:
    """
    Create new task.
    """
    task = crud.task.create(db=db, obj_in=task_in)
    return task


@router.put("/{id}", response_model=schemas.Task)
def update_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    task_in: schemas.TaskUpdate,
) -> Any:
    """
    Update an task.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task = crud.task.update(db=db, db_obj=task, obj_in=task_in)
    return task


@router.get("/{id}", response_model=schemas.Task)
def read_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get task by ID.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{id}", response_model=schemas.Task)
def delete_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an task.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task = crud.task.remove(db=db, id=id)
    return task
