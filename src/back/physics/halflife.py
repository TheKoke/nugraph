class HalfLife:
    def __init__(self, value: float, in_eV: bool = False) -> None:
        if in_eV:
            self._time = HalfLife.from_energy(value)
            self._energy = value

        self._time = value
        self._energy = HalfLife.from_time(value)

    @staticmethod
    def from_time(time: float) -> float:
        reduced_planck = 6.58e-16 # eV * s
        return reduced_planck / time

    @staticmethod
    def from_energy(energy: float) -> float:
        reduced_planck = 6.58e-16 # eV * s
        return reduced_planck / energy
    
    @property
    def time(self) -> float:
        return self._time
    
    @property
    def energy(self) -> float:
        return self._energy


if __name__ == '__main__':
    pass