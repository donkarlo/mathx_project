class Bound:
    def __init__(self, val:float, is_open:bool=False):
        self._val = val
        self._is_open = is_open

    def get_val(self)->float:
        return self._val
    def get_is_open(self)->bool:
        return self._is_open