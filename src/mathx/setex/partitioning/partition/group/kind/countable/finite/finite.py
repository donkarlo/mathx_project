from mathx.setex.kind.countable.finit.finite import Finite as BaseFiniteSet
from mathx.setex.partitioning.partition import Partition
from typing import List


class Finite(BaseFiniteSet):
    """
    this is a finit set of partitions even from an infinte or uncountable set
    """
    def __init__(self, partitions: List[Partition]):
        Finite.__init__(self, partitions)