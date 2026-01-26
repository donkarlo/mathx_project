import numpy as np

from mathx.number.kind.real.interval.unit.open_unit_interval import OpenUnitInterval
from mathx.set_nd.kind.countable.finit.finited import Finited
from mathx.set_nd.partitioning.partition.kind.subset_complement import SubsetComplement as SubsetComplementPartition


class Numbered(Finited):
    def __init__(self, members: np.ndarray):
        Finited.__init__(self, members)

    def get_random_sample_and_complement_by_ratio(self, ratio: OpenUnitInterval) -> SubsetComplementPartition:
        ratio_value = ratio.get_value()

        length = len(self._members)
        k = int(ratio_value * length)

        all_indices = np.arange(length)

        subset_indices = np.random.choice(length, size=k, replace=False)
        subset_indices = np.sort(subset_indices)

        complement_indices = np.setdiff1d(all_indices, subset_indices)

        subset = self._members[subset_indices]
        subset_sample = Finited(subset)

        complement = self._members[complement_indices]
        complement_sample = Finited(complement)

        partition = SubsetComplementPartition(subset_sample, complement_sample)

        return partition