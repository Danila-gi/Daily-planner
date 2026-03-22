from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.task import Task, TaskStatus

class TaskController:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_task(self, title: str, description: str, status: TaskStatus):
        task = Task(title=title, description=description, status=status)
        self.session.add(task)

    async def delete_task(self, task: Task):
        await self.session.delete(task)

    async def get_task_by_title(self, title: str) -> Task:
        result = await self.session.execute(
            select(Task).where(Task.title == title)
        )
        return result.scalars().first()

    async def get_all_tasks(self) -> list[Task]:
        result = await self.session.execute(select(Task))
        return result.scalars().all()

    async def update_task_data(self, title: str = None, description: str = None, status: TaskStatus = None) -> Task:
        currentTask = await self.get_task_by_title(title)
        if not currentTask:
            return None

        currentTask.title = title
        if description:
            currentTask.description = description
        if status:
            currentTask.status = status

        return currentTask

