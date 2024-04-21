from __future__ import annotations

from back.graf.node import Node
from back.graf.edge import Edge


class Graph[T]:
    def __init__(self, nodes: list[Node[T]], edges: list[Edge[T]], adjacent: list[list[float]]) -> None:
        self._nodes = nodes
        self._edges = edges
        self._adj = adjacent

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        pass

    def node_at(self, index: int) -> Node[T]:
        pass

    def find(self, val: T) -> int:
        pass


class GraphBuilder[T]:
    def __init__(self) -> None:
        self._nodes = list()
        self._edges = list()
        self._adjacent = list(list())

    def __call__(self) -> Graph:
        return Graph(self._nodes, self._edges, self._adjacent)
    
    def add_node(self) -> bool:
        pass

    def add_edge(self, index1: int, index2: int) -> bool:
        pass
    

if __name__ == '__main__':
    pass
