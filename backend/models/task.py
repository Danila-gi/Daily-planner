import enum
from sqlalchemy import Column, Integer, String, Text, Enum
from db.database import Base
from pydantic import BaseModel

class TaskStatus(str, enum.Enum):
    STARTED = "started"
    PROCESSED = "processed"
    FINISHED = "finished"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(TaskStatus), nullable=False)

class TaskData(BaseModel):
    title: str
    description: str
    status: TaskStatus

class TaskDelete(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    description: str | None
    status: TaskStatus | None