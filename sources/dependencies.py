from typing import Annotated

from fastapi import Depends, Request

from sources.services.build_service import BuildService


def get_build_service(request: Request):
    return request.app.state.build_service


BuildServiceDependency = Annotated[BuildService, Depends(get_build_service)]
