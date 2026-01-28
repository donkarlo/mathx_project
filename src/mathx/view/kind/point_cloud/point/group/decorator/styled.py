from mathx.view.kind.point_cloud.point.group.decorator.decorator import Decorator
from mathx.view.kind.point_cloud.point.group.interface import Interface
from mathx.view.kind.point_cloud.point.group.style.style import Style
from typing import Dict

class Styled(Decorator):
    def __init__(self, inner: Interface, style: Style):
        Decorator.__init__(self, inner)
        self._style = style

    def get_style(self) -> Style:
        return self._style

    def get_keyword_arguments(self)->Dict:
        return self._style.get_keyword_arguments()
