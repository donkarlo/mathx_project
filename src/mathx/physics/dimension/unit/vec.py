from mathx.linalg.matrix.vec.vec import Vec as LinalgVec

class Vec:
    def __init__(self, unit:Unit, val: LinalgVec):
        self._unit = unit
        self._val = val

    def get_unit(self)->Unit:
        return self._unit

    def get_val(self)->Vec:
        return self._val