from mathx.number.kind.real.interval.unit.open_unit_interval import OpenUnitIntervalNumber
from mathx.setex.kind.countable.finit.finite import Finite
from mathx.statistic.population.population import Population

from mathx.statistic.population.sampling.sample.kind.finite_numbers_defined_by_members import FiniteNumbersDefinedByMembers as FiniteNumbersDefinedByMembersSample
import numpy as np

from mathx.setex.partitioning.partition.group.kind.countable.kind.subset_complement import SubsetComplement as SubsetComplementPartition

class FiniteNumbersDefinedByMembers(Population, Finite):
    def __init__(self, members: np.ndarray):
        Finite.__init__(self, members)

    def get_random_sample_and_complement_by_ratio(self, ratio: OpenUnitIntervalNumber) -> SubsetComplementPartition:
        ratio_value = ratio.get_value()

        length = len(self._members)
        k = int(ratio_value * length)

        all_indices = np.arange(length)

        subset_indices = np.random.choice(length, size=k, replace=False)
        subset_indices = np.sort(subset_indices)

        complement_indices = np.setdiff1d(all_indices, subset_indices)

        subset = self._np_array[subset_indices]
        subset_sample = FiniteNumbersDefinedByMembersSample(subset)

        complement = self._np_array[complement_indices]
        complement_sample = FiniteNumbersDefinedByMembersSample(complement)

        partitions = SubsetComplementPartition([subset_sample, complement_sample])

        return partitions