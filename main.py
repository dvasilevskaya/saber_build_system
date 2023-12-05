from contextlib import asynccontextmanager

from fastapi import FastAPI

from sources.api import router
from sources.services.build_service import BuildService
from sources.utils import load_builds, load_tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.build_service = BuildService(
        builds=load_builds(),
        tasks=load_tasks()
    )
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router, prefix="/api")
