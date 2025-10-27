from mathx.linalg.tensor.tensor import Tensor
from mathx.linalg.tensor.vec.vec_representable import VecRepresentable
from typing import Union, Sequence, TYPE_CHECKING

if TYPE_CHECKING:
    from mathx.linalg.tensor.vec.row import Row
    from mathx.linalg.tensor.vec.col import Col

import numpy as np


class Vec(Tensor):
    def __init__(self, components: Union[Sequence[float], np.ndarray]) -> None:
        """
        Vec holds an array of shape (n,).
        You can convert it into a row or column vector when needed.
        - Vector is direction+magnititude, do not mistake it with point
        """
        self.__init(components)

    def set_components(self, components: Union[Sequence[float], np.ndarray]) -> None:
        self.__init(components)

    def __init(self, components: Union[Sequence[float], np.ndarray, VecRepresentable]) -> None:
        if isinstance(componets, VecRepresentable):
            components = components.get_vec_representation().get_components()
            return

        components = np.asarray(components, dtype=float)
        if components.ndim != 1:
            raise ValueError(f"Expected a flat 1D vector, got shape {self._components.shape}")
        self._components = components
        self._components_len = self._components.shape[0]
        super().__init__(self._components)

    def get_components(self) -> np.ndarray:
        """
        Return the vector as a flat array of shape (n,).
        """
        return self._components

    def __getitem__(self, item) -> float:
        return self._components[item]

    def get_dim(self) -> int:
        return self._components_len

    def get_row_vec(self) -> "Row":
        """
        Return the vector as a row vector of shape (1, n).
        """
        from mathx.linalg.tensor.vec.row import Row
        return Row(self)

    def get_col_vec(self) -> "Col":
        """
        Return the vector as a column vector of shape (n, 1).
        """
        from mathx.linalg.tensor.vec.col import Col
        return Col(self)
