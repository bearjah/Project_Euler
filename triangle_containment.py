import click
import math
from itertools import combinations
import matplotlib.pyplot as plt


def polar_to_cart(p):
    r, t = p
    x = r * math.cos(t)
    y = r * math.sin(t)
    return x, y


def cart_to_polar(p):
    x, y = p
    r = math.sqrt(x * x + y * y)
    t = math.atan2(y, x)
    return r, t


def rotate(p, rad):
    x, y = p
    rx = x * math.cos(rad) + y * math.sin(rad)
    ry = -x * math.sin(rad) + y * math.cos(rad)
    return rx, ry


def sub(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]


def line(p1, p2):
    a = (p1[1] - p2[1])
    b = (p2[0] - p1[0])
    c = (p1[0]*p2[1] - p2[0]*p1[1])
    return a, b, -c


def intersection(l1, l2):
    d  = l1[0] * l2[1] - l1[1] * l2[0]
    dx = l1[2] * l2[1] - l1[1] * l2[2]
    dy = l1[0] * l2[2] - l1[2] * l2[0]
    if d != 0:
        x = dx / d
        y = dy / d
        return x, y
    else:
        return False


@click.command()
@click.argument('source', type=click.File('r'), default='p102_triangles.txt')
def main(source: click.File):
    total_contained = 0
    for l in source:
        t = list(map(int, l.split(",")))
        points = t[0:2], t[2:4], t[4:6]
        intersection_points = {'x': [], 'y': []}
        for p1, p2 in combinations(points, 2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx != 0:
                a = dy / dx
                line_from_triangle = line(p1, p2)
                y_axis = line([0, -1000], [0, 1000])
                b = intersection(line_from_triangle, y_axis)
                if dy != 0:
                    x0 = (-b[1] / a)
                    if min(p1[0], p2[0]) <= x0 <= max(p1[0], p2[0]):
                        intersection_points['x'].append(x0)
                y0 = b[1]
                if min(p1[1], p2[1]) <= y0 <= max(p1[1], p2[1]):
                    intersection_points['y'].append(y0)
            else:
                if min(p1[1], p2[1]) <= 0 <= max(p1[1], p2[1]):
                    intersection_points['x'].append(p1[0])
        contained = False
        if any(x == 0 for x in intersection_points['x']) or any(y == 0 for y in intersection_points['y']):
            print('got 0')
        if len(intersection_points['x']) == 2 and len(intersection_points['y']) == 2:
            if (math.copysign(1, intersection_points['x'][0]) != math.copysign(1, intersection_points['x'][1])
                    and math.copysign(1, intersection_points['y'][0]) != math.copysign(1, intersection_points['y'][1])):
                contained = True
                total_contained += 1
        ix = intersection_points['x'] + [0] * len(intersection_points['y'])
        iy = [0] * len(intersection_points['x']) + intersection_points['y']
        print(contained)
        plot_triangle(t, ix, iy)
    print(total_contained)


###
#            d = sub(p1, p2)
#            p = cart_to_polar(d)
#            rotated = rotate(d, math.pi * .5)
#            # rotated[1], p1
#            # line_from_origin = p[1], [0, 0]
#            line_from_triangle = line(p1, p2)
#            line_from_origin = line([0, 0], rotated)
#            i = intersection(line_from_triangle, line_from_origin)
#            # ix.append(i[0])
#            # iy.append(i[1])
#            # ix.append(d[0])
#            # iy.append(d[1])
#            # ix.append(rotated[0])
#            # iy.append(rotated[1])
#            if i is not False:
#                ix.append(0)
#                iy.append(0)
#                ix.append(i[0])
#                iy.append(i[1])
#            # ix.append(rotated[0])
#            # iy.append(rotated[1])
#            print(p1, p2, d, p, rotated, i)

def plot_triangle(t, ix = None, iy = None):
    x = [t[i] for i in range(0, 6, 2)]
    y = [t[i] for i in range(1, 6, 2)]
    x.append(t[0])
    y.append(t[1])
    fig1, ax = plt.subplots()
    ax.set_xlim(-1000, 1000)
    ax.set_ylim(-1000, 1000)
    ax.set_box_aspect(1)
    plt.plot(x, y)
    plt.plot(ix, iy)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
