from typing import Union, Tuple
import numpy as np
from mathx.linalg.matrix.vec.col_vec import ColVec


class ThreeDColVec(ColVec):
    def __init__(self, raw_vec:Union[np.ndarray[float,float,float], Tuple[float, float, float]]):
        super().__init__(raw_vec)