from mathx.set_nd.kind.countable.finit.kind.member_mentioned.member_mentioned import MemberMentioned
import numpy as np

class Numbered(MemberMentioned):
    def __init__(self, members:np.ndarray):
        self._members = members