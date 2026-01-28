from mathx.set_nd.partitioning.partition.partition import Partition
from mathx.set_nd.set_nd import SetNd


class SubsetComplement(Partition):
    def __init__(self, subset: SetNd, complement: SetNd):
        self._subset = subset
        self._complement = complement
        Partition.__init__(self, [self._subset, self._complement])

    def get_complement(self):
        return self._complement

    def get_subset(self):
        return self._subset

    def get_universal_set(self)->SetNd:
        pass
