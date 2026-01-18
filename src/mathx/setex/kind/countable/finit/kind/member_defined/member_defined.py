from mathx.setex.kind.countable.finit.finited import Finited
from utilix.data.kind.group.group import Group


class MemberDefined(Finited):
    def __init__(self, members_group:Group):
        self._members_group = members_group
        Finited.__init__(self, self._members_group.get_members())

