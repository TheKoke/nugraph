import numpy

from back.physics.decay import Decay
from back.physics.halflife import HalfLife


class Parity:
    def __init__(self, parity: bool) -> None:
        self._p = parity

    def __str__(self) -> str:
        return '+' if self._p else '-'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __call__(self) -> bool:
        return self._p
    

class Spin:
    def __init__(self, value: float) -> None:
        self._s = value

    def __str__(self) -> str:
        if self._s % 1 == 0:
            return str(int(self._s))
        
        factor = 2
        return f'{int(self._s * factor)}/{factor}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __call__(self) -> float:
        return self._s


class State:
    def __init__(self, energy: float, spin: list[Spin], parity: list[Parity], decays: list[Decay], halflife: HalfLife) -> None:
        self._energy = energy
        self._spin = spin
        self._parity = parity
        self._decays = decays
        self._halflife = halflife

    def __str__(self) -> str:
        return f'State({round(self._energy, 3)}, {self._spin}{self._parity} MeV' + \
               f'decays: {self._decays}, halflife: {self._halflife})'

    def __repr__(self) -> str:
        return str(self)
    
    @property
    def energy(self) -> float:
        return self._energy
    
    @property
    def spin(self) -> list[Spin]:
        return self._spin
    
    @property
    def parity(self) -> list[Parity]:
        return self._parity
    
    @property
    def decays(self) -> list[Decay]:
        return self._decays
    
    @property
    def halflife(self) -> HalfLife:
        return self._halflife
    
    @property
    def is_excited_state(self) -> bool:
        return self._energy != 0.0


if __name__ == '__main__':
    pass
