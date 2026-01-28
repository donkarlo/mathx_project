from mathx.view.kind.point_cloud.point.group.interface import Interface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator):
    def __init__(self, inner:Interface):
        BaseDecorator.__init__(self, inner)