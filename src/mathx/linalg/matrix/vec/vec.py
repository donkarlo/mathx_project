from array import array
from typing import Union, Sequence
import numpy as np
from mathx.linalg.matrix.matrix import Matrix


class Vec(Matrix):
    def __init__(self, components:np.ndarray):
        "Anything here will work with numpy"
        if self._is_2d():
            super().__init__(components)
        else:
            raise ValueError(f"the dimention is neither 1×2 nor 2×1 it is {self.get_dims()}")

    def _is_2d(self) -> bool:
        if isinstance(self._raw_data, np.ndarray):
            return self._raw_data.ndim == 2

        elif isinstance(self._raw_data, (list, tuple)):
            if not self._raw_data:
                return False

            # Handle inner array.array
            if all(isinstance(row, array.array) for row in self._raw_data):
                row_length = len(self._raw_data[0])
                return all(len(row) == row_length for row in self._raw_data)

            # Handle inner list/tuple
            if all(isinstance(row, (list, tuple)) for row in self._raw_data):
                row_length = len(self._raw_data[0])
                return all(len(row) == row_length for row in self._raw_data)

        return False