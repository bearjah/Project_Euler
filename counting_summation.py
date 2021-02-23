import numpy as np


def counting_summation(n):
    ways = np.zeros(n+1)
    ways[0] = 1
    for i in range(1, n):
        for j in range(i, n+1):
            ways[j] += ways[j - i]
            # print(ways[j], j, i)
    return ways[n]


if __name__ == '__main__':
    print('sum ways count:', counting_summation(100))
