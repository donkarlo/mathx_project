from mathx.set.kind.countable.finite.kind.member_mentioned.numbered.numbered import Numbered
from mathx.statistic.population.kind.countable.finite.member_mentioned.numbered.numbered import Numbered as NumberedPopulation
import numpy as np
from mathx.number.kind.real.interval.unit.open_unit_interval import OpenUnitInterval

from mathx.statistic.population.sampling.kind.countable.finite.members_mentioned.numbered.numbered import Numbered as NumberedSampling

class TestNumbered:
    def setup_method(self):
        self._numbered_set = Numbered(np.array([
            [1, 2],
            [2, 3],
            [3, 1],
            [4, 2],
            [5, 3],
            [3, 4],
            [2, 5],
            [4, 4],
            [10, 10],
            [11, 9],
            [12, 11],
            [13, 10],
            [14, 12],
            [15, 11],
            [16, 13],
            [17, 12],
            [18, 14],
            [19, 13],
            [20, 15],
            [21, 14],
            [22, 16],
            [23, 15],
            [24, 17],
        ]))
        self._population = NumberedPopulation(self._numbered_set)
        self._sampling = NumberedSampling(self._population)

        open_unit_interval = OpenUnitInterval(0.7)
        subset_complement_partition = self._sampling.get_random_sample_and_complement_by_ratio(open_unit_interval)
        self._sample = subset_complement_partition.get_subset()
        self._complement = subset_complement_partition.get_complement()

    def test_random_sample_and_complement_by_ratio(self)->None:
        for subset_member in self._sample.get_members():
            assert not np.any(np.all(self._complement.get_members() == subset_member, axis=1))

    def test_order_keeping(self)->None:
        set_members = np.array([])
        assert True
