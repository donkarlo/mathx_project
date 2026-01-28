from mathx.set.set import Set
from mathx.statistic.population.population import Population
from abc import ABC, abstractmethod

class Sampling(ABC):
    def __init__(self, population:Population):
        self._population = population

    @abstractmethod
    def get_sample_set(self)->Set:
        pass

    @abstractmethod
    def get_complement_set(self) -> Set:
        pass


    def get_population(self):
        return self._population

