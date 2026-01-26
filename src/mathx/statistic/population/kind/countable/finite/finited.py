from mathx.statistic.population.kind.countable.countable import Countable

class Finited(Countable):
    def __init__(self, members):
        Countable.__init__(self, members)