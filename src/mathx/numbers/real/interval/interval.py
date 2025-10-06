


class Interval:
    def __init__(self, lowerbound: float, upperbound: float):
        self._lowerbound = lowerbound
        self._upperbound = upperbound

    def get_lowerbound(self) -> float:
        return self._lowerbound
    def get_upperbound(self) -> float:
        return self._upperbound