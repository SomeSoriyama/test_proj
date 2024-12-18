from contextlib import asynccontextmanager

from fastapi import FastAPI

from db import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    print('Старт')
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова к работе')
    yield
    print('Выключение')



app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


if __name__ == '__main__':
    from uvicorn import run
    run(app, port=80, log_level="info")
