from mathx.set.set import Set
from mathx.statistic.population.kind.countable.finite.finite import Finite


class MembersMentioned(Finite):
    def __init__(self, set: Set):
        Finite.__init__(self, set)