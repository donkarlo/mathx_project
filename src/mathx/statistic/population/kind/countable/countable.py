from mathx.statistic.population.population import Population


class Countable(Population):
    def __init__(self, members):
        Population.__init__(self, members)