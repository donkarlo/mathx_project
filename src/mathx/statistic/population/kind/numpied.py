import numpy as np

from mathx.number.kind.real.interval.unit.open_unit_interval import OpenUnitInterval
from mathx.setex.kind.countable.finit.finited import Finited
from mathx.setex.partitioning.partition.kind.subset_complement import SubsetComplement as SubsetComplementPartition
from mathx.statistic.population.population import Population
from utilix.data.kind.group.group import Group


class Numpied(Population):
    def __init__(self, members: np.ndarray):
        Population.__init__(self, members)
        self._members = members
        self._members_group = Group(self._members)

    def get_members_group(self) -> Group:
        return self._members_group

    def get_random_sample_and_complement_by_ratio(self, ratio: OpenUnitInterval) -> SubsetComplementPartition:
        ratio_value = ratio.get_value()

        length = len(self._members)
        k = int(ratio_value * length)

        all_indices = np.arange(length)

        subset_indices = np.random.choice(length, size=k, replace=False)
        subset_indices = np.sort(subset_indices)

        complement_indices = np.setdiff1d(all_indices, subset_indices)

        subset = self._np_array[subset_indices]
        subset_sample = Finited(subset)

        complement = self._np_array[complement_indices]
        complement_sample = Finited(complement)

        partition = SubsetComplementPartition(subset_sample, complement_sample)

        return partition