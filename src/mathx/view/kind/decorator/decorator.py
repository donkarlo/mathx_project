from mathx.view.interface import Interface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator):
    def __init__(self, inner:Interface):
        BaseDecorator.__init__(self, inner)