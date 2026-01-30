class Sample:
    def __init__(self, size: int):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        self._size = size
