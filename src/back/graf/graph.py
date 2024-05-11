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
        self._nodes: list[Node] = list()
        self._edges: list[Edge] = list()
        self._adjacent = list(list())

    def __call__(self) -> Graph:
        return Graph(self._nodes, self._edges, self._adjacent)
    
    def add_node(self, pretend: Node[T]) -> bool:
        if not isinstance(pretend.val, T):
            return False
        
        self._nodes.append(pretend)
        return True

    def add_edge(self, origin: int, destination: int) -> bool:
        if origin < 0 or origin >= len(self._nodes) or destination < 0 and destination >= len(self._nodes):
            return False
        
        self._nodes[origin].add_neighbor(self._nodes[destination])
        return False
    

if __name__ == '__main__':
    pass
