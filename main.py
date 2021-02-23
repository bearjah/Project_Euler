from typing import Tuple, List, Optional
import click
import numpy as np
from astar import AStar
import scipy as sc
import math


def distinct_prime_factor(consecutive_count):
    consecutive_found = False
    consecutive_num_list = np.zeros(consecutive_count)
    consecutive_num_list[0] = 6
    consecutive_num_list[1] = 7
    # consecutive_num_list[2] = 4
    # consecutive_num_list[3] = 5
    while consecutive_found is False:
        if check_distinct_primes(consecutive_num_list):
            consecutive_found = True
        consecutive_num_list += consecutive_count


def get_primes(num):
    prime_list = []
    for i in range(2, int(num)+1):
        if num % i == 0:
            if check_prime(i):
                prime_list.append(i)
    return prime_list


def check_distinct_primes(num_list):
    prime_list = []
    for num in num_list:
        prime_list = get_primes(num)
        print(prime_list)


# def valid_path(row, ind):
#
def get_max_node(row):
    curr_max = 0
    curr_max_index = 0
    for i in range(row):
        if row[i] > curr_max:
            curr_max = row[i]
            curr_max_index = i
    return curr_max, curr_max_index


def find_maximum_sum(triangle):
    max_sum = [(triangle[0][0], (0, 0))]
    found_max_path = False
    while found_max_path:
        for i in range(1, len(triangle) + 1):
            max_in_node = get_max_node(triangle[i])
            print(max_in_node)
        # while valid_path()
    print(max_sum)


def maximum_path_sum():
    triangle = ([3], [7, 4], [2, 4, 6], [8, 5, 9, 3])
    # print(triangle[2])
    return find_maximum_sum(triangle)

#     [3]
#    [7, 4]
#   [2, 4, 6]
#  [8, 5, 9, 3]
# [1, 3, 2, 4, 12]

Triangle = List[List[int]]
Index = Tuple[int, int]


def get_lower_neighbor_indices(t: Triangle, idx: Index) -> Tuple[Index, Index]:
    x, y = idx
    down = x + 1
    if down > len(t) - 1:
        return None, None
    return (x + 1, y), (x + 1, y + 1)


def get_upper_neighbor_indices(t: Triangle, idx: Index) -> Tuple[Optional[Index], Optional[Index]]:
    x, y = idx
    up = x - 1
    if up < 0:
        return None, None

    upper_left = (up, y - 1)
    upper_right = (up, y)
    if upper_left[1] < 0:
        upper_left = None
    if upper_right[1] < 0 or y > up:
        upper_right = None

    return upper_left, upper_right


def get(t: Triangle, dest: Index) -> int:
    return t[dest[0]][dest[1]]


def get_single_path_value(t: Triangle, dest: Index) -> int:
    value = get(t, dest)
    left, right = get_upper_neighbor_indices(t, dest)
    if not(left or right):
        return value
    left_sum = get_single_path_value(t, left) if left else None
    right_sum = get_single_path_value(t, right) if right else None
    return value + max(filter(None, (left_sum, right_sum)))


def get_path_value(t: Triangle) -> int:
    return max(get_single_path_value(t, (len(t) - 1, y)) for y in range(len(t)))


def get_path_value_2(t: Triangle) -> int:
    sums = []
    for x, line in enumerate(t):
        line_sums = []
        for y in range(len(line)):
            curr_sum = line[y] + max(sums[idx[1]] if idx else 0 for idx in get_upper_neighbor_indices(t, (x, y)))
            line_sums.append(curr_sum)
        sums = line_sums
    return max(sums)


class Solver(AStar):
    def __init__(self, triangle: Triangle):
        self.triangle = triangle

    def heuristic_cost_estimate(self, n1: Index, n2: Index):
        x1, y1 = n1
        x2, y2 = n2
        return math.hypot(x2 - x1, y2 - y1) * 99

    def distance_between(self, n1: Index, n2: Index):
        return get(self.triangle, n2)

    def neighbors(self, node: Index):
        return list(filter(None, get_upper_neighbor_indices(self.triangle, node)))


def get_path_value_astar(t: Triangle) -> int:
    t = t + [[0] * (len(t) + 1)]
    print(t)
    solver = Solver(t)
    path_sum = lambda path: sum(get(t, idx) for idx in path)
    return max(path_sum(solver.astar((len(t) - 1, y), (0, 0))) for y in range(len(t)))


@click.command()
@click.argument('source', type=click.File('r'))
def main(source: click.File):
    triangle = [list(map(int, l.split())) for l in source]
    print(triangle)
    # triangle = triangle[:20]
    # found_path = list(MazeSolver(triangle).astar((0, 0), (3, 0)))
    # print(sum(get(triangle, idx) for idx in found_path))

    # print(triangle)
    # print(f"{get_lower_neighbor_indices(triangle, (0, 0))} {get_upper_neighbor_indices(triangle, (1, 0))}")
    # print(f"{get_path_value(triangle)}")
    print(f"{get_path_value_2(triangle)}")
    # print(f"{get_path_value_astar(triangle)}")


if __name__ == '__main__':
    main()
    # print('distinct_prime_factor:', distinct_prime_factor(2))
    # print('maximum path sum', maximum_path_sum())
