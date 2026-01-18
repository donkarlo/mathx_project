from mathx.setex.partitioning.partition.partition import Partition
from mathx.setex.setex import Setex


class SubsetComplement(Partition):
    def __init__(self, subset: Setex, complement: Setex):
        self._subset = subset
        self._complement = complement
        Partition.__init__(self, [self._subset, self._complement])

    def get_complement(self):
        return self._complement

    def get_subset(self):
        return self._subset

    def get_universal_set(self)->Setex:
        pass
