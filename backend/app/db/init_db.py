from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import base  # noqa: F401

from app.db.base_class import Base  # noqa
from app.db.session import engine  # noqa

def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)