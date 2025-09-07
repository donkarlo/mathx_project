class Vecs:
    def __init__(self, unit:Unit, vecs:List[Vec]):
        self._unit = unit
        self._vecs = vecs

    def add_vec(self, vec:Vec):
        self._vecs.append(vec)

    def add_united_vec(self, united_vec:UnitedVec):
        if united_vec.get_unit().get_type_id() != self._unit.get_type_id():
            raise ValueError(f"")