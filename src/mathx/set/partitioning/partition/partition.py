from mathx.set_nd.set_nd import SetNd
from typing import List


class Partition(SetNd):
    def __init__(self, partions: List[SetNd]):
        self._partions = partions

    def get_partitions(self) -> List[SetNd]:
        return self._partions
