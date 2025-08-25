class SupportingDimensionUnits:
    """
    This class determines which dimension type is matchable with which units
    """
    def __init__(self, dimension_type:DimensionType, unit_types:List[UnitType]):
        self._dimension_type = dimension_type
        self._unit_types = unit_types