from mathx.linalg.vec.vec import Vec
from physix.dimension.unit.vec import Vec as UnitedVec

class Quaternion(Vec):
    """i² = j² = k² = ijk = −1
    ij = k, jk = i, ki = j
    ji = −k, kj = −i, ik = −j"""
    __slots__ = ("_qw", "_qx", "_qy", "_qz")
    def __init__(self, qw:float, qx:float, qy:float, qz:float):
        self._qw = qw
        self._qx = qx
        self._qy = qy
        self._qz = qz
        super().__init__([self._qw,self._qx,self._qy,self._qz])

    def normalize(self):
        pass

    def conjugate(self):
        pass

    def multiply(self, other:"Quaternion"):
        pass

    def from_axis_angle(self, axis:float, theta:float):
        pass