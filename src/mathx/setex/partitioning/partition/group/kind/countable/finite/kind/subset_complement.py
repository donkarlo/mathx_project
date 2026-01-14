from mathx.setex.partitioning.partition.group.kind.countable.finite.finite import Finite as FinitePartitionGroup
from mathx.setex.setex import Setex


class SubsetComplement(FinitePartitionGroup):
    def __init__(self, subset:Setex, complement:Setex):
        self._subset = subset
        self._complement = complement
        FinitePartitionGroup.__init__(self, [self._subset, self._complement])

    def get_complement(self):
        return self._complement
    def get_subset(self):
        return self._subset