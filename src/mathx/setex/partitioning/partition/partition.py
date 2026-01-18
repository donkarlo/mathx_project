from mathx.setex.setex import Setex
from typing import List


class Partition(Setex):
    def __init__(self, partions: List[Setex]):
        self._partions = partions

    def get_partitions(self) -> List[Setex]:
        return self._partions
