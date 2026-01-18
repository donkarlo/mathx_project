from typing import Any


class Setex:
    """

    """
    def __init__(self, members:Any):
        self._members = members

    def get_members(self)->Any:
        return self._members