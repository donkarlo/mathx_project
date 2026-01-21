from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from typing import Union

@runtime_checkable
class Interface(Protocol):

    def build(self) -> None: ...

    def render(self) -> None: ...

    def get_dimension(self) -> int: ...

    def get_pyplot_axis(self) -> Union[Axes, Axes3D]: ...

    def get_pyplot_figure(self) -> Figure: ...