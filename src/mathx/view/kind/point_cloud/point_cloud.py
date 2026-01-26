import matplotlib.pyplot as plt

from mathx.view.pair_set.pair_set import PointSet
from mathx.view.view import View


class PointCloud(View):
    def __init__(self, point_set: PointSet) -> None:
        View.__init__(self, point_set)

    def build(self) -> None:
        plt.scatter(*self.get_point_group().get_members())

    def show(self) -> None:
        View.show(self)