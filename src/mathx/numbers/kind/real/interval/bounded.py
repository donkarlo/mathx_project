from mathx.numbers.kind.real.interval.interval import Interval


class Bounded:
    def __init__(self, val: float, interval: Interval) -> None:
        # TODO: check the bounds
        self._val: float = val
