import numpy as np
from mathx.view.kind.point_cloud.decorator.decorator import Decorator
from mathx.view.kind.point_cloud.decorator.lined.group_pair_seted.group_pair_seted import GroupPairSeted


class OrderedInterLineConnected(Decorator):
    def __init__(self, inner:GroupPairSeted):
        if not isinstance(inner, GroupPairSeted):
            raise TypeError("Inner Type must be GroupPairSeted")
        Decorator.__init__(self, inner)

    def build(self) -> None:
        group_pair_seted_view = self.get_inner()
        group_pair_set_members = group_pair_seted_view.get_group_pair_set().get_members()
        group_pair_seted_view.build()
        axis = group_pair_seted_view.get_pyplot_axis()
        for  pair_set in group_pair_set_members:
            pair_set_members = pair_set.get_members()
            axis.plot(*pair_set_members)


    def render(self) -> None:
        self.get_inner().render()


    def example_to_remove(self):
        import matplotlib.pyplot as plt
        import numpy as np

        # Example data
        x1 = np.array([0, 1, 2, 3])
        y1 = np.array([1, 2, 1, 2])

        x2 = np.array([0, 1, 2, 3])
        y2 = np.array([2, 1, 2, 1])

        fig, ax = plt.subplots()

        # Scatter points for both datasets
        ax.scatter(x1, y1)
        ax.scatter(x2, y2)

        # Connect corresponding points
        for i in range(len(x1)):
            ax.plot([x1[i], x2[i]], [y1[i], y2[i]])

        plt.show()

if __name__ == "__main__":
    oilc = OrderedInterLineConnected(null)