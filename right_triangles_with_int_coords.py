import numpy as np


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        rep = '(' + str(self.x) + ', ' + str(self.y) + ')'
        return rep

    def __sub__(self, other):
        if isinstance(other, Coordinate):
            return self.x - other.x, self.y - other.y

    def __ne__(self, other):
        if isinstance(other, Coordinate):
            return bool(self.x != other.x or self.y != other.y)


class Triangle:
    def __init__(self, points):
        point0 = points[0]
        point1 = points[1]
        point2 = points[2]
        # print("points : ", point0, point1, point2)
        op = point1 - point0
        pq = point2 - point1
        qo = point2 - point0
        self.lines = [op, pq, qo]
        # print(self.lines)


def count_triangles(n):
    count = 0
    origin = Coordinate(0, 0)
    possible_coords = [Coordinate(x, y) for x in range(n + 1) for y in range(n+1) if Coordinate(x, y) != origin]
    print(repr(possible_coords))
    for p1 in possible_coords:
        for p2 in possible_coords:
            if p1.x == p2.x and p1.y == p2.y:
                continue
            triangle = Triangle([origin, p1, p2])
            for i in range(len(triangle.lines)):
                for j in range(i, len(triangle.lines)):
                    if triangle.lines[i] == triangle.lines[j]:
                        continue
                    if np.dot(triangle.lines[i], triangle.lines[j]) == 0:
                        print(triangle.lines[i], triangle.lines[j])
                        count += 1
    return count/2


if __name__ == '__main__':
    print(count_triangles(50))
