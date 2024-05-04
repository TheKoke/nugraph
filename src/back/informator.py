from back.physics.state import State
from back.ensdf.parser import NAME2CHARGE, CHARGE2NAME


class Informator:

    @staticmethod
    def is_exist(z: int, a: int) -> bool:
        pass

    @staticmethod
    def name_of(z: int, a: int) -> str:
        pass

    @staticmethod
    def mass_excees(z: int, a: int) -> float:
        pass

    @staticmethod
    def states(z: int, a: int) -> list[State]:
        pass

    @staticmethod
    def discharges(z: int, a: int) -> list[tuple[State, State]]:
        pass

    @staticmethod
    def energy_levels(z: int, a: int) -> list[float]:
        pass

    @staticmethod
    def spins(z: int, a: int) -> list[float]:
        pass

    @staticmethod
    def parities(z: int, a: int) -> list[bool]:
        pass


if __name__ == '__main__':
    pass
