from mathx.set.set import Set
from mathx.statistic.population.population import Population


class Countable(Population):
    def __init__(self, set: Set):
        Population.__init__(self, set)