from typing import List

from mathx.linalg.tensor.vector.vector_representable import VectorRepresentable
from mathx.geometry.euclidean.shape.type.point.point import Point as BasePoint


class Point(BasePoint, VectorRepresentable):
    def __init__(self, coordinates:List[float]):
        if len(coordinates) != 3:
            raise ValueError("number of coordinates must be 3")
        super().__init__(coordinates)