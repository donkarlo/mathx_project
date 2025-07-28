from mathx.linalg.matrix.vec.vec import Vec
from mathx.unit.united_val import UnitedVal

class UnitedScalar(UnitedVal):
    def __init__(self, val:float):
        super().__init__(Vec([val]))
        self._val = val

