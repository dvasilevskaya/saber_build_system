from sources.exceptions import ItemNotFoundError
from sources.utils import TopologicalSort


class BuildService:
    def __init__(self, builds: dict, tasks: dict):
        self.__builds = builds
        self.__tasks = tasks

    def get_tasks(self, build: str, full: bool = False) -> list[str]:
        build_tasks = self.__builds.get(build)
        if not build_tasks:
            raise ItemNotFoundError(
                f"Build with name '{build}' "
                f"does not exist or has no dependent tasks!"
            )

        sorted_tasks = TopologicalSort(build_tasks, self.__tasks).sort()
        if full is False:
            build_tasks = set(build_tasks)
            sorted_tasks = [
                task
                for task in sorted_tasks
                if task in build_tasks
            ]

        return sorted_tasks
