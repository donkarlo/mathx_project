from abc import ABC, abstractmethod
from typing import Any

def Interface(ABC, Protocol):
    _members: Any
    @abstractmethod
    def __init__(self, _members:Any):
        ...

