from mathx.plot.kind.scatter.decorator.decorator import Decorator
from mathx.plot.kind.scatter.interface import Interface
import numpy as np
from typing import List
from mathx.view.kind.decorator.multi_data_set import MultiDataSet


class PairLineConnected(Decorator):
    def __init__(self, inner:MultiDataSet, datas:List[np.nd_array]):
        Decorator.__init__(self, inner, datas)