import numpy

from back.state import State
from back.ensdf.informator import Informator


class Nuclei:
    def __init__(self, z: int, a: int) -> None:
        if not Informator.is_exist(z, a):
            raise ValueError(f'Nuclei with z={z} and a={a} does not exist!')
        
        self._z = z
        self._a = a
        self._name = Informator.name_of(z, a)


if __name__ == '__main__':
    pass
