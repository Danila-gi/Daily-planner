from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from db.dependencies import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession
from models.task import TaskData, TaskDelete, TaskUpdate
from controllers.task_controller import TaskController

router = APIRouter()


@router.post("/add-task")
async def add_task(task: TaskData, session=Depends(get_db_session)):
    taskController = TaskController(session)
    currentTaskInDB = await taskController.get_task_by_title(task.title)
    if currentTaskInDB:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Задача уже существует"}
        )
    await taskController.add_task(task.title, task.description, task.status)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Задача добавлена"}
    )


@router.delete("/delete-task")
async def delete_task(task: TaskDelete, session=Depends(get_db_session)):
    taskController = TaskController(session)
    currentTaskInDB = await taskController.get_task_by_title(task.title)
    if not currentTaskInDB:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Задача не найдена"}
        )
    await taskController.delete_task(currentTaskInDB)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Задача удалена"}
    )

@router.put("/update-task")
async def update_task(task: TaskUpdate, session=Depends(get_db_session)):
    taskController = TaskController(session)
    currentTaskInDB = await taskController.get_task_by_title(task.title)
    if not currentTaskInDB:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Задача не найдена"}
        )
    await taskController.update_task_data(task.title, task.description, task.status)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Задача обновлена"}
    )

@router.get("/get-task")
async def get_task(title: str, session=Depends(get_db_session)):
    taskController = TaskController(session)
    currentTaskInDB = await taskController.get_task_by_title(title)
    if not currentTaskInDB:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Задача не найдена"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"title": currentTaskInDB.title,
                 "description": currentTaskInDB.description,
                 "status": currentTaskInDB.status.value}
    )

@router.get("/get-all-tasks")
async def get_all_task(session=Depends(get_db_session)):
    taskController = TaskController(session)
    allTasks = await taskController.get_all_tasks()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "tasks": [
                {
                    "title": task.title,
                    "description": task.description,
                    "status": task.status.value
                }
                for task in allTasks
            ],
            "total": len(allTasks)
        }
    )