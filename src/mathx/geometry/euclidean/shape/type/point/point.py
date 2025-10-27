from mathx.geometry.euclidean.shape.shape import Shape
from mathx.linalg.tensor.vec.vec import Vec
from mathx.linalg.tensor.vec.vec_representable import VecRepresentable

class Point(Shape, VecRepresentable):
    def __init__(self, coordinates:List[float]):
        self._coordinates = coordinates
        
        self._vec_representation = None

    def get_vec_representation(self):
        self._vec_representation = Vec(self._coordinates)
        return self._vec_representation


