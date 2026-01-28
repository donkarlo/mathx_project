import numpy as np

from mathx.view.interface import Interface
from mathx.view.kind.point_cloud.decorator.decorator import Decorator


class OrderedIntraLineConnected(Decorator):
    def __init__(self, inner:Interface):
        Decorator.__init__(self, inner)

    def _build(self) -> None:
        np_point_group= self.get_inner().get_point_group().get_members()
        self.get_inner().get_axis().plot(*np_point_group.T)


    def render(self) -> None:
        self.get_inner().render()