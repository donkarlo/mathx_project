import numpy as np
from mathx.linalg.tensor.vec.vec import Vec


class TwoOpranded:
    def __init__(self, left_vec: Vec, right_vec: Vec):
        self._left_vec = left_vec
        self._right_vec = right_vec

    def get_concated(self) -> Vec:
        """
        Concatenate left and right vectors into a new Vec.
        """
        combined = np.concatenate((
            self._left_vec.get_components(),
            self._right_vec.get_components()
        ))
        return Vec(combined)
