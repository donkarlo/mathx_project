from mathx.statistic.population.sampling.sampler.kind.countable.countable import Countable
from mathx.statistic.population.kind.countable.finite.finite import Finite
from mathx.statistic.population.sampling.sampler.size.size import Size


class Finite(Countable):
    def __init__(self, population:Finite, size:Size):
        Countable.__init__(self, population, size)
