from mathx.number.kind.real.interval.unit.close_unit_interval_number import CloseUnitIntervalNumber
from mathx.statistic.population.sampling.sampler.size.size import Size


class Ratio(Size):
    def __init__(self, ratio: CloseUnitIntervalNumber, population_length:int):
        self._ratio = ratio
        self._size_value = int(self._ratio.get_value() * population_length)
        Size.__init__(self, self._size_value)