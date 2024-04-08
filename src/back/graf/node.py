from __future__ import annotations


class Node[T]:
    def __init__(self, val: T, neighrs: list[T]) -> None:
        self._val = val
        self._neighrs = neighrs

    @property
    def val(self) -> T:
        return self._val
    
    @property
    def neighrs(self) -> T:
        return self.neighrs[:]
    
    def add_neighbor(self, pretend: Node) -> bool:
        pass
    

if __name__ == '__main__':
    pass
