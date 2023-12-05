import pytest

from sources.exceptions import ItemNotFoundError
from sources.services.build_service import BuildService


def test_build_service():
    build_service = BuildService(
        builds={
            "test_1": ["1", "0"]
        },
        tasks={
            "0": ["5", "4"],
            "1": ["3", "4"],
            "2": ["5"],
            "3": ["2"],
            "4": [],
            "5": [],
        }
    )
    with pytest.raises(ItemNotFoundError):
        build_service.get_tasks("build_doesnt_exist")

    tasks = build_service.get_tasks("test_1")
    assert tasks == ["0", "1"]

    tasks = build_service.get_tasks("test_1", full=True)
    assert tasks == ["5", "4", "0", "2", "3", "1"]
