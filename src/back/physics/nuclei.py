import numpy

from back.physics.state import State
from back.informator import Informator


class Nuclei:
    def __init__(self, z: int, a: int) -> None:
        if not Informator.is_exist(z, a):
            raise ValueError(f'Nuclei with z={z} and a={a} does not exist!')
        
        self._z = z
        self._a = a
        self._name = Informator.name_of(z, a)
        self._states = Informator.states(z, a)
        self._discharges = Informator.discharges(z, a)

    @property
    def charge(self) -> int:
        return self._z
    
    @property
    def nuclons(self) -> int:
        return self._a

    @property
    def name(self) -> int:
        return self._name
    
    @property
    def states(self) -> list[State]:
        return self._states.copy()
    
    def __str__(self) -> str:
        return f'{self._a}{self._name}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __hash__(self) -> int:
        return hash(str(self))


if __name__ == '__main__':
    pass
