from mathx.numbers.kind.real.interval.bound import Bound


class OpenBound(Bound):
    def __init__(self, val: float):
        super().__init__(val, False)
