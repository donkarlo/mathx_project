from mathx.view.kind.point_cloud.decorator.decorator import Decorator
from mathx.view.kind.point_cloud.interface import Interface
from mathx.view.pair_set.pair_set import PairSet
from mathx.view.pair_set.group.Group import Group as PairSetGroup
from matplotlib import pyplot as plt

class GroupPairSeted(Decorator):
    def __init__(self, inner:Interface, pair_set_group: PairSetGroup):
        Decorator.__init__(self, inner)
        self._pair_set_group = pair_set_group
        self.add_pair_set(self._inner.get_pair_set())

    def get_group_pair_set(self)-> PairSetGroup:
        return self._pair_set_group

    def show(self)->None:
        for pair_set in self._pair_set_group.get_members():
            plt.scatter(*pair_set.get_members().T)


    def add_pair_set(self, pair_set:PairSet)->None:
        self._pair_set_group.add_member(pair_set)