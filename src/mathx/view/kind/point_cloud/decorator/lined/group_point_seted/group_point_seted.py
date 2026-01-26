from mathx.view.kind.point_cloud.decorator.decorator import Decorator
from mathx.view.kind.point_cloud.interface import Interface
from mathx.view.kind.point_cloud.point.group.group import Group as PointGroup
from matplotlib import pyplot as plt
from

class MultiplePointGrouped(Decorator):
    def __init__(self, inner:Interface, multiple_point_group: List[PointGroup]):
        Decorator.__init__(self, inner)
        self._point_group_group = multiple_point_group

    def get_group_pair_set(self)-> PointGroup:
        return self._point_group_group

    def show(self)->None:
        for pair_set in self._point_group_group.get_members():
            plt.scatter(*pair_set.get_members().T)


    def add_point_group(self, point_group: PointGroup)->None:
        self._point_group_group.add_member(point_group)