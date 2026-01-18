from abc import ABC

from mathx.setex.setex import Setex
from mathx.statistic.population.interface import Interface as PopulationInterface
from typing import Any

class Population(PopulationInterface, Setex, ABC):
    """
    Here they are exclusively numerical populations
    """
    def __init__(self, members: Any):
        Setex.__init__(self, members)