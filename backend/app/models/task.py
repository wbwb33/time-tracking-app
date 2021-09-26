from sqlalchemy import Column, Integer, String, Date, Time, Float

from app.db.base_class import Base


class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    task_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    duration = Column(Float)
