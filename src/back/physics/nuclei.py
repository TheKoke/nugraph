from __future__ import annotations

import numpy

from back.physics.state import State
from back.informator import Informator


class Nuclei:
    def __init__(self, z: int, a: int) -> None:
        if not Informator.is_exist(z, a):
            raise ValueError(f'Nuclei with z={z} and a={a} does not exist!')
        
        self._z = z
        self._a = a
        self._delta_m = Informator.mass_excees(z, a)
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
    def mass_excees(self) -> float:
        return self._delta_m
    
    @property
    def states(self) -> list[State]:
        return self._states.copy()
    
    @property
    def discharges(self) -> list[tuple[State, State]]:
        return self._discharges.copy()
    
    @property
    def mass(self) -> float:
        proton = 938.27  # MeV
        neutron = 939.57 # MeV
        return proton * self._z + neutron * (self._a - self._z)
    
    @property
    def radius(self) -> float:
        fermi = 1.28 # fm
        return fermi * numpy.cbrt(self._a)
    
    def __str__(self) -> str:
        return f'{self._a}{self._name}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __hash__(self) -> int:
        return hash(str(self))
    
    def __eq__(self, other: Nuclei) -> bool:
        if not isinstance(other, Nuclei):
            return False
        
        return self._z == other.charge and self._a == other.nuclons
    
    def __add__(self, other: Nuclei) -> Nuclei:
        if not isinstance(other, Nuclei):
            raise RuntimeError(f'Cannot apply "+" opearator to instance of Nuclei and {other.__class__}.')
        
        return Nuclei(self._z + other.charge, self._a + other.nuclons)
    
    def __sub__(self, other: Nuclei) -> Nuclei:
        if not isinstance(other, Nuclei):
            raise RuntimeError(f'Cannot apply "-" opearator to instance of Nuclei and {other.__class__}.')
        
        if other.charge >= self._z or other.nuclons >= self._a:
            raise RuntimeError(f'Cannot subtract nuclei from nuclei with same nucleons and charge.')
        
        return Nuclei(self._z - other.charge, self._a - other.nuclons)
    
    def sharp_radius(self) -> float:
        return 1.28 * numpy.cbrt(self._a) - 0.76 + 0.8 * numpy.cbrt(1 / (self._a)) # fm
    
    def central_radius(self) -> float:
        sharp_radii = self.sharp_radius()
        return sharp_radii * (1 - (1 / sharp_radii) ** 2)


if __name__ == '__main__':
    pass
