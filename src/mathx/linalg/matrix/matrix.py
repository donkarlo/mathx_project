import numpy as np
import numpy.typing as npt

from typing import Annotated, Union, List, Tuple
import array

MatrixLike = Union[
    Annotated[npt.NDArray[np.float64], ("n", "m")],                # NumPy 2D
    Annotated[List[List[float]], ("n", "m")],                      # list of lists
    Annotated[Tuple[Tuple[float, ...], ...], ("n", "m")],          # tuple of tuples
    Annotated[Tuple[npt.NDArray[np.float64], ...], ("n", "m")],    # tuple of NumPy arrays
    Annotated[List[array.array], ("n", "m")],                      # list of array.array (Python's built-in)
    Annotated[Tuple[array.array, ...], ("n", "m")]                 # tuple of array.array
]

class Matrix:
    def __init__(self, raw_data: MatrixLike):
        self._raw_data = raw_data
        if not self.__is_valid_2d():
            raise TypeError("Expected a 2D array-like structure (n × m)")
        self._np_rows = np.asarray(self._raw_data)

    def get_dims(self)->tuple[int, int]:
        return self._np_rows.shape

    def get_dims_with_multi_sign(self)->str:
        rows, cols = self._np_rows.shape
        return f"{rows} × {cols}"
