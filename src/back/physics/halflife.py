import numpy


class HalfLife:
    def __init__(self, value: float, in_eV: bool = False) -> None:
        if in_eV:
            self._time = HalfLife.from_energy(value)
            self._energy = value

        self._time = value
        self._energy = HalfLife.from_time(value)

    @staticmethod
    def from_time(time: float) -> float:
        pass

    @staticmethod
    def from_energy(energy: float) -> float:
        pass


if __name__ == '__main__':
    pass