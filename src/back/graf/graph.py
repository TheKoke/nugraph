from __future__ import annotations

from back.graf.node import Node
from back.graf.edge import Edge


class Graph[T]:
    def __init__(self, nodes: list[Node[T]], edges: list[Edge[T]], adjacent: list[list[float]]) -> None:
        pass


class GraphBuilder[T]:
    def __init__(self) -> None:
        self._nodes = list()
        self._edges = list()
        self._adjacent = list(list())

    def __call__(self) -> Graph:
        return Graph(self._nodes, self._edges, self._adjacent)
    

if __name__ == '__main__':
    pass
