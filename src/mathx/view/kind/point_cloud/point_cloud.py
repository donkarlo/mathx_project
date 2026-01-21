import matplotlib.pyplot as plt

from mathx.view.pair_set.pair_set import PairSet
from mathx.view.view import View


class PointCloud(View):
    def __init__(self, pair_set: PairSet) -> None:
        View.__init__(self, pair_set)

    def build(self) -> None:
        plt.scatter(*self.get_pair_set().get_members())

    def show(self) -> None:
        View.show(self)