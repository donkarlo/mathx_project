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
        self.__raw_data = raw_data
        if not self.__is_valid_2d():
            raise TypeError("Expected a 2D array-like structure (n × m)")
        self.__np_rows = np.asarray(self.__raw_data)

    def __is_valid_2d(self) -> bool:
        if isinstance(self.__raw_data, np.ndarray):
            return self.__raw_data.ndim == 2

        elif isinstance(self.__raw_data, (list, tuple)):
            if not self.__raw_data:
                return False

            # Handle inner array.array
            if all(isinstance(row, array.array) for row in self.__raw_data):
                row_length = len(self.__raw_data[0])
                return all(len(row) == row_length for row in self.__raw_data)

            # Handle inner list/tuple
            if all(isinstance(row, (list, tuple)) for row in self.__raw_data):
                row_length = len(self.__raw_data[0])
                return all(len(row) == row_length for row in self.__raw_data)

        return False
