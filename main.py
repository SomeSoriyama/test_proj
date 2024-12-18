from contextlib import asynccontextmanager

from fastapi import FastAPI

from db import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(current_app: FastAPI):
    print('Старт')
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова к работе')
    yield current_app
    print('Выключение')


if __name__ == '__main__':
    app = FastAPI(lifespan=lifespan)
    app.include_router(tasks_router)
