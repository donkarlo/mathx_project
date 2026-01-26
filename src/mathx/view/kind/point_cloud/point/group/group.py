import numpy as np

from utilix.data.kind.group.group import Group as BaseGroup
from typing import Union, List

class Group(BaseGroup):
    def __init__(self, members: Union[np.ndarray, List]):
        BaseGroup.__init__(self, members)
    def get_column_by_index(self, index:int)-> Union[np.ndarray, List]:
        return self.get_members()[:index]