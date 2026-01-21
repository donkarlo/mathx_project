import numpy as np

from mathx.view.interface import Interface
from mathx.view.kind.point_cloud.decorator.decorator import Decorator


class OrderedIntraLineConnected(Decorator):
    def __init__(self, inner:Interface):
        Decorator.__init__(self, inner)

    def build(self) -> None:
        pair_set= np.asarray(self.get_inner().get_pair_set().get_members())
        self.get_inner().get_pyplot_axis().plot(*pair_set.T)


    def render(self) -> None:
        self.get_inner().render()