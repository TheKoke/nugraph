from __future__ import annotations

from back.graf.node import Node
from back.graf.edge import Edge


class Graph[T]:
    def __init__(self, nodes: list[Node[T]], edges: list[Edge[T]], adjacent: list[list[float]]) -> None:
        self._nodes = nodes
        self._edges = edges
        self._adj = adjacent

    @property
    def nodes(self) -> list[Node[T]]:
        return self._nodes[:]
    
    @property
    def edges(self) -> list[Edge[T]]:
        return self._edges[:]
    
    @property
    def adjacent(self) -> list[list[float]]:
        return self._adj[:]

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'Graph(nodes={len(self._nodes)}, edges={len(self._edges)})'

    def node_at(self, index: int) -> Node[T]:
        if index < 0 or index >= len(self._nodes):
            return None

        return self._nodes[index]

    def find(self, val: T) -> int:
        for i in range(len(self._nodes)):
            if self._nodes[i].val == val:
                return i
            
        return -1


class GraphBuilder[T]:
    def __init__(self) -> None:
        self._nodes: list[Node] = list()
        self._edges: list[Edge] = list()
        self._adjacent = list()

    def __call__(self) -> Graph:
        return Graph(self._nodes, self._edges, self._adjacent)
    
    def add_node(self, pretend: Node[T]) -> bool:
        if not isinstance(pretend.val, T):
            return False
        
        self._nodes.append(pretend)
        self.extend_adjacent()
        
        return True

    def add_edge(self, origin: int, destination: int, weight: float = 1.0) -> bool:
        if origin < 0 or origin >= len(self._nodes) or destination < 0 and destination >= len(self._nodes):
            return False
        
        self._edges.append(Edge.create_edge(self._nodes[origin], self._nodes[destination], weight))
        
        self._adjacent[origin][destination] = weight
        self._adjacent[destination][origin] = weight

        return True
    
    def extend_adjacent(self) -> None:
        self._adjacent.append([])
        for i in range(len(self._adjacent)):
            self._adjacent[i].append(0)
    

if __name__ == '__main__':
    pass
