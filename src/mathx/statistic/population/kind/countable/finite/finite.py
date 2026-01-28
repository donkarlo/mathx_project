from mathx.set.set import Set
from mathx.statistic.population.kind.countable.countable import Countable

class Finite(Countable):
    def __init__(self, set: Set):
        Countable.__init__(self, set)