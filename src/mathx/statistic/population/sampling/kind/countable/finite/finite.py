from mathx.statistic.population.sampling.kind.countable.countable import Countable as CountableSampling
from mathx.statistic.population.kind.countable.finite.finite import Finite


class Finite(CountableSampling):
    def __init__(self, population:Finite):
        CountableSampling.__init__(self, population)
