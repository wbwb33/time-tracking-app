from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    def get_with_date_as_filter(
        self, db: Session, task_date: str, skip: int = 0, limit: int = 100
    ) -> List[Task]:
        return (
            db.query(self.model)
            .filter(Task.task_date == task_date)
            .offset(skip)
            .limit(limit)
            .all()
        )


task = CRUDTask(Task)
