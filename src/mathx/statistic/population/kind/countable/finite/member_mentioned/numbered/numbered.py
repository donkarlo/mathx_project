from mathx.set.set import Set
from mathx.statistic.population.kind.countable.finite.member_mentioned.members_mentioned import MembersMentioned

class Numbered(MembersMentioned):
    def __init__(self, set: Set):
        MembersMentioned.__init__(self, set)

