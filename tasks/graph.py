from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        result = []

        def dive(element):
            if element not in result:
                result.append(element)
            if len(element.outbound) > 0:
                for next_el in element.outbound:
                    if next_el in result:
                        continue
                    dive(next_el)

        dive(self._root)
        return result

    def bfs(self) -> list[Node]:
        result = []
        visited = []

        def walk(element):
            if element not in result:
                result.append(element)
                visited.append(element)
            if len(element.outbound) > 0:
                for next_el in element.outbound:
                    if next_el not in result:
                        result.append(next_el)
                for next_el in element.outbound:
                    if next_el not in visited:
                        walk(next_el)

        walk(self._root)
        return result
