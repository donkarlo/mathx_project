from mathx.number.type_hint.type_hint import REAL_SUBSETS

class CloseUnitIntervalNumber:
    def __init__(self, value: REAL_SUBSETS):
        self._value = value
        if value <= 0 or value >= 1:
            raise ValueError("The value is not between 0 and 1")

    def get_value(self) -> REAL_SUBSETS:
        return self._value
