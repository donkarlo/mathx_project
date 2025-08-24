from mathx.linalg.matrix.vec.vec import Vec

class UnitedVec:
    def __init__(self, unit:Unit, val:Vec):
        self._unit = unit
        self._val = val
