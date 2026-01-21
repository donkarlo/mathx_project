from typing import Protocol, runtime_checkable

from mathx.setex.interface import Interface as SetInterface

@runtime_checkable
class Interface(SetInterface, Protocol):
    pass