from mathx.set_nd.kind.countable.finit.finited import Finited


class MemberMentioned(Finited):
    def __init__(self, members):
        Finited.__init__(self, members)