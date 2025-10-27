import numpy as np
from typing import List
from mathx.linalg.tensor.vec.vec import Vec


class ManyOperanded:
    def __init__(self, vec_list: List[Vec]):
        # store a list of Vec objects
        self._vec_list = vec_list

    def get_concated(self) -> Vec:
        # concatenate components from all Vecs into a single Vec
        if not self._vec_list:
            raise ValueError("The vector list is empty.")

        # start with the components of the first Vec
        concated = self._vec_list[0].get_components()

        # concatenate the rest
        for vec in self._vec_list[1:]:
            concated = np.concatenate((concated, vec.get_components()))

        return Vec(concated)
