from typing import Union, Sequence, TYPE_CHECKING

if TYPE_CHECKING:
    from mathx.linalg.vec.row import Row
    from mathx.linalg.vec.col import Col

import numpy as np


class Vec:
    def __init__(self, components: Union[Sequence[float], np.ndarray]) -> None:
        """
        Vec holds an array of shape (n,).
        You can convert it into a row or column vector when needed.
        """
        self._components = np.asarray(components, dtype=float)
        if self._components.ndim != 1:
            raise ValueError(f"Expected a flat 1D vector, got shape {self._components.shape}")

        self._components_len = self._components.shape[0]

    def get_components(self) -> np.ndarray:
        """
        Return the vector as a flat array of shape (n,).
        """
        return self._components

    def get_dim(self)->int:
        return self._components_len


    def get_row_vec(self) -> "Row":
        """
        Return the vector as a row vector of shape (1, n).
        """
        from mathx.linalg.vec.row import Row
        return Row(self)

    def get_col_vec(self) -> "Col":
        """
        Return the vector as a column vector of shape (n, 1).
        """
        from mathx.linalg.vec.col import Col
        return Col(self)


