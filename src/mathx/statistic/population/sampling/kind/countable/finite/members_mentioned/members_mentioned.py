from mathx.statistic.population.kind.countable.finite.member_mentioned.members_mentioned import MembersMentioned
from mathx.statistic.population.sampling.kind.countable.finite.finite import Finite


class MembersMentioned(Finite):
    def __init__(self, population:MembersMentioned):
        Finite.__init__(self, population)