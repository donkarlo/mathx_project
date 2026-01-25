from abc import ABC, abstractmethod
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.axes import Axes
from mathx.view.pair_set.pair_set import PairSet
from typing import Union
from matplotlib.figure import Figure
from types import ModuleType
import numpy as np


class View(ABC):
    def __init__(self, pair_set: PairSet):
        self._pair_set = pair_set
        pair_set_members = np.asarray(self._pair_set.get_members())
        #TODO for the moment from here it is nd array
        if pair_set_members.ndim != 2 or pair_set_members.shape[1] not in (2, 3):
            raise ValueError("pair_set must be a 2D array with shape (n, 2) or (n, 3)")

        self._dimension = None
        self._pyplot_figure = plt.figure()
        if pair_set_members.shape[1] == 2:
            self._pyplot_axis = self._pyplot_figure.add_subplot(111)
            self._dimension = 2
        elif pair_set_members.shape[1] == 3:
            self._pyplot_axis = self._pyplot_figure.add_subplot(111, projection='3d')
            self._dimension = 3

    def get_pair_set(self) -> PairSet:
        return self._pair_set

    def get_pyplot_axis(self) -> Union[Axes, Axes3D]:
        return self._pyplot_axis

    def get_pyplot_figure(self) -> Figure:
        return self._pyplot_figure

    def get_pyplot(self)-> ModuleType:
        return plt

    @abstractmethod
    def build(self):
        """
        To add all data sets etc
        Returns:

        """
        pass

    def render(self):
        plt.show()
