from typing import Protocol
class VecRepresentable(Protocol):
    _vec_representation:Vec
    """For things whic are reppresentable by vector"""
    def get_vec_representation(self)->Vec: ...