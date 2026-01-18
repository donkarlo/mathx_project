from mathx.plot.kind.scatter.decorator.decorator import Decorator
from mathx.plot.kind.scatter.interface import Interface
import numpy as np
from typing import List

class PairLineConnected(Decorator):
    def __init__(self, inner:Interface, datas:List[np.nd_array]):
        Decorator.__init__(self, inner, datas)