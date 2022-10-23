from numpy import pi
from numpy import exp
from numpy import sqrt
from numpy import array
from numpy.linalg import norm
from random import uniform


class PointHandler:
    i = 1j
    RANGE = (0, 2 * pi)

    @classmethod
    def get_point(cls):
        point = exp(cls.i * uniform(*cls.RANGE))
        x, y = point.real, point.imag
        return x, y


def euclidean_norm(x, y):
    result = norm(array(x) - array(y))
    return result


def color(distance):
    return "r" if distance < sqrt(3) else "b"
