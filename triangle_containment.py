import matplotlib.pyplot as plt


def main():
    with open('p102_triangles.txt', 'r') as source:
        triangles = [list(map(int, l.split(","))) for l in source]
    t_print = 0
    for t in triangles:
        x = [t[i] for i in range(0, 6, 2)]
        y = [t[i] for i in range(1, 6, 2)]
        x.append(t[0])
        y.append(t[1])
        t_print += 1
        if t_print == 2:
            plt.plot(x, y)
            plt.show()
    coordinates = []
    for t in triangles:
        coordinates.append([(t[i], t[i+1]) for i in range(0, 6, 2)])


if __name__ == '__main__':
    main()
