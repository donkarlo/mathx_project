from mathx.geometry.euclidean.shape.shape import Shape
from mathx.linalg.tensor.vector.vector import Vector
from mathx.linalg.tensor.vector.vector_representable import VectorRepresentable

class Point(Shape, VectorRepresentable):
    def __init__(self, coordinates:List[float]):
        self._coordinates = coordinates
        
        self._vec_representation = None

    def get_vector_representation(self):
        self._vec_representation = Vector(self._coordinates)
        return self._vec_representation


