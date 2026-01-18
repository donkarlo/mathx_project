from abc import ABC
from typing import Protocol

from mathx.setex.interface import Interface as SetInterface


class Interface(SetInterface, ABC, Protocol):
    pass