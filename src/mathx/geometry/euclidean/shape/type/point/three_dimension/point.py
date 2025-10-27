from typing import List

from mathx.linalg.tensor.vec.vec_representable import VecRepresentable
from mathx.geometry.euclidean.shape.type.point.point import Point as BasePoint


class Point(BasePoint,VecRepresentable):
    def __init__(self, coordinates:List[float]):
        if len(coordinates) != 3:
            raise ValueError("number of coordinates must be 3")
        super().__init__(coordinates)