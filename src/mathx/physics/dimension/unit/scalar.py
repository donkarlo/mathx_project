from mathx.linalg.matrix.vec.vec import Vec
from mathx.physics.unit.united_val import UnitedVal
from mathx.physics.unit.unit import Unit

class Scalar:
    def __init__(self, unit:Unit, value:float):
        self._unit = unit
        self._value = value

