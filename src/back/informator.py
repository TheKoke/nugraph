from back.physics.decay import Decay
from back.physics.state import State
from back.ensdf.parser import NAME2CHARGE, CHARGE2NAME, ENSDFParser


class Informator:

    @staticmethod
    def is_exist(z: int, a: int) -> bool:
        return ENSDFParser.is_exist(z, a)

    @staticmethod
    def name_of(z: int) -> str:
        if z in CHARGE2NAME:
            return CHARGE2NAME[z]

    @staticmethod
    def mass_excees(z: int, a: int) -> float:
        if Informator.is_exist(z, a):
            return ENSDFParser.mass_excees(z, a)

    @staticmethod
    def states(z: int, a: int) -> list[State]:
        if Informator.is_exist(z, a):
            collected_states = ENSDFParser.states(z, a)

            states = []
            for i in range(collected_states):
                energy = collected_states[0]
                spins = collected_states[1]
                parities = collected_states[2]
                decays = [Decay.from_string(string) for string in collected_states[3]]
                halflife = collected_states[4]

                states.append(State(energy, spins, parities, decays, halflife))

            return states

    @staticmethod
    def discharges(z: int, a: int) -> list[tuple[State, State]]:
        origins, destinations = ENSDFParser.discharges(z, a)
        states = Informator.states(z, a)

        discharges = []
        for i in range(len(origins)):
            origin = next(state for state in states if state.energy == origins[i])
            destination = next(state for state in states if state.energy == destinations[i])

            discharges.append((origin, destination))

        return discharges


if __name__ == '__main__':
    pass
