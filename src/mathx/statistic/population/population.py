from mathx.statistic.population.interface import Interface as PopulationInterface
from typing import Any


class Population(PopulationInterface):
    """
    Here they are exclusively numerical populations
    """
    def __init__(self, members):
        self._members = members

    def get_members(self)->Any:
        return self._members