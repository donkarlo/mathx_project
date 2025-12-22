from typing import Set, List

class Sets:
    def __init__(self, sets_list: List[Set]):
        self._set_lists = sets_list
    def get_set_lists(self) -> List[Set]:
        return self._set_lists