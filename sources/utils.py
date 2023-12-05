from collections import defaultdict

import yaml

from sources.conf import settings


class TopologicalSort:
    def __init__(self, vertices, dependency_pool):
        self.graph = defaultdict(list)
        self.__init(vertices.copy(), dependency_pool)

    def __init(self, vertices, dependency_pool):
        while vertices:
            vertex = vertices.pop()
            dependencies = dependency_pool[vertex]
            self.graph[vertex].extend(dependencies)
            vertices.extend(dependencies)

    def __sort(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.__sort(i, visited, stack)

        stack.append(v)

    def sort(self) -> list:
        visited = dict.fromkeys(self.graph.keys(), False)
        stack = []

        for i in self.graph:
            if not visited[i]:
                self.__sort(i, visited, stack)

        return stack


def load_tasks() -> dict:
    with open(settings.tasks_path) as file:
        return {
            task["name"]: task["dependencies"]
            for task in yaml.load(file, Loader=yaml.FullLoader)["tasks"]
        }


def load_builds() -> dict:
    with open(settings.builds_path) as file:
        return {
            build["name"]: build["tasks"]
            for build in yaml.load(file, Loader=yaml.FullLoader)["builds"]
        }
