import numpy as np
import numpy.typing as npt

type ScalarType = int | float | np.integer | np.floating
type TensorType = ScalarType | npt.NDArray[np.number]