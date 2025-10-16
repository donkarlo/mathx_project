from mathx.numbers.real.interval.interval import Interval


class ClosedUnitInterval(Interval):
    def __init__(self):
        super().__init__(LowerBound(0, False), LowerBound(0, False))