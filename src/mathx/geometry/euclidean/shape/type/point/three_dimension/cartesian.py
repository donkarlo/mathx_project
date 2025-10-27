from mathx.linalg.tensor.vec.vec import Vec


class Cartesian(Vec):
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
        super(Vec).__init__([self._x, self._y])

    def to_cartesian(self) -> "Cartesian":
        return self

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def change_origin(self, origin: Vec):
        pass
