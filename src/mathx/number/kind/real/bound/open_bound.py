from mathx.numbers.kind.real.bound.bound import Bound


class OpenBound(Bound):
    def __init__(self, value: float):
        super().__init__(value, False)
