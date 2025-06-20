from mathx.linalg.matrix.vec import Vec


class RowVec(Vec):
    def __init__(self,row):
        self._row=row