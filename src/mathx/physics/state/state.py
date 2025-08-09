from typing import Union
from mathx.linalg.matrix.vec.col_vec import ColVec
from mathx.linalg.matrix.vec.row_vec import RowVec


class State:
    '''
    This is a physical state
    '''
    def __init__(self, vec:ColVec, id:Union[int,str]=None):
        self._col_vec:ColVec = vec
        self.__id:Union[int,str] = id

    def get_id(self) -> Union[int,str]:
        return self.__id

    def get_col_vec(self) -> ColVec:
        return self._col_vec

    def get_row_vec(self) -> RowVec:
        return self._col_vec.transpose()
