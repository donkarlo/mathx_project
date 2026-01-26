from abc import ABC

from mathx.set_nd.set_nd import SetNd
from mathx.statistic.population.interface import Interface as PopulationInterface
from typing import Any

class Population(PopulationInterface, SetNd, ABC):
    """
    Here they are exclusively numerical populations
    """
    def __init__(self, members: Any):
        SetNd.__init__(self, members)