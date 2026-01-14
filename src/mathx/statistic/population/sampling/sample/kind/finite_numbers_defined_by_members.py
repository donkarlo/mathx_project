from mathx.setex.kind.countable.finit.finite import Finite
from mathx.statistic.population.population import Population
from mathx.statistic.population.sampling.sample.sample import Sample
import numpy as np

class FiniteNumbersDefinedByMembers(Sample, Finite):
    def __init__(self, members:np.ndarray, population:Population):
        Sample.__init__(self, population)
        Finite.__init__(self, members)