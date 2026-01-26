from typing import Union, List

from mathx.view.pair_set.pair_set import PointSet
from utilix.data.kind.group.group import Group as BaseGroup
import numpy as np

class Group(BaseGroup):
    def __init__(self, pair_set: PointSet):
        BaseGroup.__init__(self, pair_set)