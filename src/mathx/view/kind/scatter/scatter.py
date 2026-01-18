from mathx.plot.kind.point_wise.interface import Interface as PointWiseInterface

from mathx.view.data_set.data_set import DataSet
from mathx.view.view import View


class Scatter(View, PointWiseInterface):
    def __init__(self, data_set:DataSet) -> None:
        View.__init__(self, data_set)
