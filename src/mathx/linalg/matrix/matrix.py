import numpy as np

from mathx.linalg.matrix.matrix_like_data_type import MatrixLikeDataType


class Matrix:
    def __init__(self, raw_data: MatrixLikeDataType):
        self._raw_data = raw_data
        if not self.__is_valid_2d():
            raise TypeError("Expected a 2D array-like structure (n × m)")
        self._np_rows = np.asarray(self._raw_data)

    def get_dims(self) -> tuple[int, int]:
        return self._np_rows.shape

    def get_dims_with_multi_sign(self) -> str:
        rows, cols = self._np_rows.shape
        return f"{rows} × {cols}"

    def transpose(self) -> "Matrix":
        """Return a new Matrix object that is the transpose of this one."""
        transposed_data = self._np_rows.T
        return Matrix(transposed_data)

    def __is_valid_2d(self) -> bool:
        try:
            arr = np.asarray(self._raw_data)
            return arr.ndim == 2
        except Exception:
            return False

    def transpose(self) -> "Matrix":
        return Matrix(self._np_rows.T)

    def is_square(self) -> bool:
        return self._np_rows.shape[0] == self._np_rows.shape[1]

    def pinv(self, rcond: float = 1e-15) -> "Matrix":
        """Moore-Penrose pseudoinverse via SVD; works for any shape."""
        return Matrix(np.linalg.pinv(self._np_rows, rcond=rcond))

    def rank(self, tol: float | None = None) -> int:
        """Numerical rank via SVD; works for any shape."""
        s = np.linalg.svd(self._np_rows, compute_uv=False)
        if tol is None:
            tol = max(self._rows, self._cols) * np.finfo(float).eps * np.max(s)
        return int(np.sum(s > tol))

    def gram_AtA(self) -> "Matrix":
        """A^T A (square, symmetric, PSD)."""
        return Matrix(self._np_rows.T @ self._np_rows)

    def gram_AAt(self) -> "Matrix":
        """A A^T (square, symmetric, PSD)."""
        return Matrix(self._np_rows @ self._np_rows.T)

    def get_rows_count(self) -> int:
        return self.get_dims()[0]

    def get_columns_count(self) -> int:
        return self.get_dims()[1]
