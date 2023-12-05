from pydantic import BaseModel, Field, RootModel


class TasksRequestModel(BaseModel):
    build: str = Field(..., description="Build name")
    full: bool | None = Field(False, description="Include all dependencies")


TasksResponseModel = RootModel[list[str | int]]
