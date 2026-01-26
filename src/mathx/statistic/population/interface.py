from typing import Protocol, runtime_checkable

from mathx.set_nd.interface import Interface as SetInterface

@runtime_checkable
class Interface(SetInterface, Protocol):
    pass