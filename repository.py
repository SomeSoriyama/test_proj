from sqlalchemy import select

from db import new_session, TaskORM
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskORM(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> tuple[STask, ...]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            try:
                return tuple(map(STask.model_validate, result.scalars().all()))
            except Exception as e:
                print(f'Validating failed: {e}')