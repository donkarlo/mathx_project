class UnitInterval(float):
    """A real number constrained to the closed unit interval [0, 1]."""

    def __new__(cls, x: float):
        if not (0.0 <= x <= 1.0):
            raise ValueError("Value must be within [0, 1].")
        return super().__new__(cls, x)