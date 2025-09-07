from typing import TypeVar, Generic, List
from mathx.physics.unit.Vecs import Vecs
from mathx.physics.unit.Unit import Unit

T = TypeVar('T')

class Scalars(Vecs, Generic[T]):
    def __init__(self, unit:Unit, scalars:List[T]):
        self._unit = unit
        self._scalars = scalars