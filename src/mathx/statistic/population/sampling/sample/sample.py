from abc import ABC

from mathx.statistic.population.population import Population


class Sample(ABC):
    def __init__(self, population):
        self._population = population

    def get_population(self)->Population:
        return self._population
