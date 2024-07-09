from __future__ import annotations

from enum import Enum


class DecayType(Enum):
    STABLE = 0
    ALPHA = 1
    BETHA_MINUS = 2
    BETHA_PLUS = 3
    ELECTRON_CAPTURE = 4
    PROTON = 5
    NEUTRON = 6
    ISOMERIC_TRANSITION = 7
    SPONTANEOUS_FISSION = 8
    CLUSTER_DECAY = 9


class Decay:
    def __init__(self, type: DecayType) -> None:
        self._type = type

    @property
    def type(self) -> DecayType:
        return self.type

    def __call__(self, z: int, a: int) -> tuple[int, int]:
        match self._type:
            case DecayType.STABLE:
                return z, a
            case DecayType.ALPHA:
                return z - 2, a - 4
            case DecayType.BETHA_MINUS:
                return z + 1, a
            case DecayType.BETHA_PLUS, DecayType.ELECTRON_CAPTURE:
                return z - 1, a
            case DecayType.PROTON:
                return z - 1, a - 1
            case DecayType.NEUTRON:
                return z, a - 1
            case DecayType.ISOMERIC_TRANSITION:
                return z, a
            case DecayType.SPONTANEOUS_FISSION:
                return None # more information is needed.
            case DecayType.CLUSTER_DECAY:
                return None # more information is needed.
            
    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        return str(self)
    
    @staticmethod
    def from_string(string: str) -> Decay:
        pass


if __name__ == '__main__':
    pass
