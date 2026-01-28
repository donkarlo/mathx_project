from mathx.set.set import Set
from mathx.statistic.population.interface import Interface as PopulationInterface

class Population(PopulationInterface):
    """
    Here they are exclusively numerical populations
    """
    def __init__(self, set: Set):
        self._set = set

    def get_set(self)->Set:
        return self._set