from typing import TypeVar, Generic, List

T = TypeVar('T')

class UnitedScalars(UnitedVecs):
    def __init__(self, unit:Unit, scalars:List[T]):
        self._unit = unit
        self._scalars = scalars