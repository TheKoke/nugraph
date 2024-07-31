from __future__ import annotations
from back.graf.node import Node


class Edge[T]:
    def __init__(self, _from: Node[T], _to: Node[T], w: float = 1.0, is_oriented: bool = False) -> None:
        self._from = _from
        self._to = _to
        self._w = w

    @property
    def from_node(self) -> Node[T]:
        return self._from
    
    @property
    def to_node(self) -> Node[T]:
        return self._to
    
    @property
    def weight(self) -> float:
        return self._w
    
    @staticmethod
    def create_edge[NT](_from: Node[NT], _to: Node[NT], weight: float = 1.0, oriented: bool = False) -> Edge[NT]:
        if oriented:
            success = _from.add_neighbor(_to)
        else:
            success = _from.add_neighbor(_to) and _to.add_neighbor(_from)
            
        if not success:
            return None

        return Edge(_from, _to, weight, oriented)
    

if __name__ == '__main__':
    pass
