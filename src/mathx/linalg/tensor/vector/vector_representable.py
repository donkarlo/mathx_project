from mathx.linalg.tensor.tensor_representable import TensorRepresentable
from typing import Protocol, runtime_checkable, TYPE_CHECKING

if TYPE_CHECKING:
    from mathx.linalg.tensor.vector.vector import Vector


@runtime_checkable
class VectorRepresentable(TensorRepresentable, Protocol):
    _vec_representation: "Vector"
    """For things whic are reppresentable by vector"""
    def get_vector_representation(self)-> "Vector": ...