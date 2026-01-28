from mathx.statistic.population.sampling.sampling import Sampling
from mathx.statistic.population.kind.countable.countable import Countable

class Countable(Sampling):
    def __init__(self, population: Countable):
        Sampling.__init__(self, population)