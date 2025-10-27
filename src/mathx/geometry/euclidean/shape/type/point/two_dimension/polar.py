import numpy as np
from mathx.geometry.euclidean.shape.type.point.two_dimension.cartesian import Cartesian
from mathx.linalg.tensor.vec.vec import Vec
from typing import List, override
from mathx.geometry.euclidean.shape.type.point.point import Point


class Polar(Point):
    def __init__(self, radius, xy_angle):
        self._radius = radius
        self._xy_angle = xy_angle
        super().__init__([self._radius, self._xy_angle])

    @overrides
    def get_cartesian(self) -> Cartesian:
        x = self._radius * np.cos(self._xy_angle)
        y = self._radius * np.sin(self._xy_angle)
        return Cartesian(x, y)

    @override
    @classmethod
    def init_from_cartesian(cls, vec: Vec) -> "Polar":
        x = vec[0]
        y = vec[1]
        radius = np.sqrt(x * x + y * y)
        angle = np.arctan2(y, x)
        return cls(radius, angle)

    @staticmethod
    def get_collection_by_radiuses_and_angle_increase_rate(radises: List[float], angle_increase_rate: float, start:float) -> List[
        "Polar"]:
        polars = []
        for radius_count, radius in enumerate(radises):
            angle = start + radius_count * angle_increase_rate
            polar = Polar(radius, angle)
            polars.append(polar)
        return polars

    @staticmethod
    def get_cartesian_by_radiuses_and_angle_increase_rate(radises: List[float], angle_increase_rate: float, start: float)->List[Cartesian]:
        cartesians = []
        for radius_count, radius in enumerate(radises):
            angle = start + radius_count * angle_increase_rate
            polar = Polar(radius, angle)
            cartezian = polar.get_cartesian()
            cartesians.append(cartezian)
        return polars