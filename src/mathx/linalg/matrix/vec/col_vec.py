from typing import Union
import numpy as np
from typing import Tuple
from typing import List


class ColVec:
    '''
    The main responsibility of this class is to represent column vector form of a vector.
    Np.ndarray usually uses rows to show vectors but mathmaticians usually use the cilumn form
    '''
    def __init__(self, raw_vec:Union[np.ndarray, Tuple[float,...], List[float,...]]):
        '''
        @todo convert row lists and np.ndarrays and tuples etc to an np.ndarray column such as [[],...[]]
        :param raw_vec:
        '''
        self._col_vec = None
        if isinstance(raw_vec, np.ndarray):
            if raw_vec.shape == (1,):
                #convert to a column
                raw_vec = raw_vec.reshape(1, -1)
                self._col_vec = raw_vec

    def extend_vertically(self, extension:"ColVec")->None:
        self._col_vec = np.vstack((self._col_vec, extension))
