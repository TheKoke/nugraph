from __future__ import annotations


class Node[T]:
    def __init__(self, val: T, neighrs: list[T]) -> None:
        self._val = val
        self._neighrs = neighrs

    @property
    def val(self) -> T:
        return self._val
    
    @property
    def neighrs(self) -> list[Node[T]]:
        return self.neighrs[:]
    
    def __hash__(self) -> int:
        return hash(str(self))
    
    def __str__(self) -> str:
        return f'Node(val={self._val})'

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Node[T]):
            casted: Node[T] = value
            return self.val == casted.val

        return False
    
    def add_neighbor(self, pretend: Node) -> bool:
        if not isinstance(pretend.val, T):
            return False
        
        self._neighrs.append(pretend)
        return True
    
    def delete_neighbor(self, neighbor: Node) -> bool:
        if not isinstance(neighbor.val, T):
            return False
        
        if neighbor not in self._neighrs:
            return False
        
        self._neighrs.pop(self._neighrs.index(neighbor))
        return True
    

if __name__ == '__main__':
    pass
