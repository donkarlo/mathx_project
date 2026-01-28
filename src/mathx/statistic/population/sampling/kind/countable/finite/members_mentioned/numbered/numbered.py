from mathx.number.kind.real.interval.unit.open_unit_interval import OpenUnitInterval
from mathx.set.kind.countable.finite.finite import Finite
from mathx.statistic.population.kind.countable.finite.member_mentioned.numbered.numbered import Numbered as NumberedPopulation
from mathx.statistic.population.sampling.kind.countable.finite.members_mentioned.members_mentioned import \
    MembersMentioned as MembersMentionedSampling
from mathx.statistic.population.sampling.sampling import Sampling
import numpy as np
from mathx.set.partitioning.partition.kind.subset_complement import SubsetComplement as SubsetComplementPartition

class Numbered(MembersMentionedSampling):
    def __init__(self, population: NumberedPopulation):
        Sampling.__init__(self, population)

    def get_random_sample_and_complement_by_ratio(self, sample_size_ratio: OpenUnitInterval) -> SubsetComplementPartition:
        """
        if you give 0.7 then the sample will be 70 pwercent and the complemet will be 30 percent
        Args:
            sample_size_ratio:

        Returns:

        """
        sample_size_ratio = sample_size_ratio.get_value()

        length = len(self._members)
        k = int(sample_size_ratio * length)

        all_indices = np.arange(length)

        subset_indices = np.random.choice(length, size=k, replace=False)
        subset_indices = np.sort(subset_indices)

        complement_indices = np.setdiff1d(all_indices, subset_indices)

        subset = self._members[subset_indices]
        subset_sample = Finite(subset)

        complement = self._members[complement_indices]
        complement_sample = Finite(complement)

        partition = SubsetComplementPartition(subset_sample, complement_sample)

        return partition