import matplotlib.pyplot as plt

from numpy import sqrt
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation
from _helpers import PointHandler
from _helpers import color
from _helpers import euclidean_norm

TRIANGLE_POINTS = {"x": (0, sqrt(3) / 2, -sqrt(3) / 2, 0), "y": (1, -1 / 2, -1 / 2, 1)}


def main():

    plt.style.use('dark_background')
    figure, ax = plt.subplots(figsize=(8, 8))
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)

    def animate(_: int):
        point_1 = PointHandler.get_point()
        point_2 = PointHandler.get_point()
        current_norm = euclidean_norm(point_1, point_2)
        current_color = color(current_norm)
        line_obj = Line2D((point_1[0], point_2[0]), (point_1[1], point_2[1]),
                          color=current_color,
                          linewidth=.3)
        ax.add_line(line_obj)

    Drawing_uncolored_circle = plt.Circle((0, 0), 1, fill=False)
    plt.plot(TRIANGLE_POINTS["x"], TRIANGLE_POINTS["y"], color='w')
    ax.add_artist(Drawing_uncolored_circle)

    animation = FuncAnimation(figure, animate, frames=600, interval=20)
    plt.show()


if __name__ == "__main__":
    main()
