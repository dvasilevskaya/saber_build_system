from fastapi import APIRouter, HTTPException, status

from sources.dependencies import BuildServiceDependency
from sources.exceptions import ItemNotFoundError
from sources.schemas.tasks import TasksRequestModel, TasksResponseModel

router = APIRouter(
    tags=["tasks"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/")
async def get_tasks(
        build: TasksRequestModel,
        build_service: BuildServiceDependency
) -> TasksResponseModel:
    """Get build tasks sorted"""
    try:
        return build_service.get_tasks(**build.model_dump())
    except ItemNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
