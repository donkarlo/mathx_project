from mathx.numbers.real.interval.bound import Bound

class ClosedBound(Bound):
    def __init__(self, val: float):
        super().__init__(val, False)