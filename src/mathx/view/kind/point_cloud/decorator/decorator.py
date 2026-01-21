from typing import Union

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from mathx.view.interface import Interface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(Interface, BaseDecorator):
    def __init__(self, inner: Interface):
        BaseDecorator.__init__(self, inner)

    def render(self) -> None:
        self.get_inner().render()

    def build(self) -> None:
        self.get_inner().build()

    def get_dimension(self) -> int:
        self.get_inner().get_dimension()

    def get_axis(self) -> Union[Axes, Axes3D]:
        self.get_inner().get_axis()

    def get_figure(self) -> Figure:
        self.get_inner().get_figure()
