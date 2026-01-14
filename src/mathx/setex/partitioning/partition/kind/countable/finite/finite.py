from mathx.setex.kind.countable.finit.finite import Finite as FinitSet
from mathx.setex.partitioning.partition import Partition as BasePartition


class Finite(BasePartition, FinitSet):
    def __init__(self, members):
        Finite.__init__(self, members)