from abc import ABC
import numpy as np

from mathx.plot.kind.scatter.style.style import Style
import matplotlib.pyplot as plt

class View(ABC):
    def __init__(self, data_set: np.ndarray):
        if data_set.ndim != 2 or data_set.shape[1] not in (2, 3):
            raise ValueError("data_set must be a 2D array with shape (n, 2) or (n, 3)")

        self._fig = plt.figure()
        if data_set.shape[1] == 2:
            self._ax = self._fig.add_subplot(111)
        elif data_set.shape[1] == 3:
            from mpl_toolkits.mplot3d import Axes3D
            self._ax = self._fig.add_subplot(111, projection='3d')

        self._pairs_set.append(data_set)

    def show(self):
        plt.show()
