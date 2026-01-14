from mathx.setex.kind.countable.countable import Countable
from utilix.data.kind.group.group import Group
import numpy as np

class Finite(Countable, Group):
    def __init__(self, members:np.ndarray):
        Group.__init__(self, members)