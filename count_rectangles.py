import math
import numpy as np


def count_rectangles(n, threshold, max_height):
    height = 1
    width = 1
    rec_count = 0
    while n - rec_count > threshold:
        rec_count = 0
        if height < max_height:
            height += 1
        else:
            width += 1
        for M in range(height):
            for N in range(width):
                rec_count += (binom(height-M, 1) * binom(width-N, 1))
    return rec_count, height, width, height*width


def find_optimal_area(n, threshold):
    best_rect_count = 0
    best_height = 0
    best_width = 0
    best_area = 0
    max_height = 100
    for i in range(2, max_height):
        curr, height, width, area = count_rectangles(n, threshold, i)
        if np.absolute(n - curr) < np.absolute(n - best_rect_count):
            best_rect_count = curr
            best_height = height
            best_width = width
            best_area = area

    return 'area = ', best_area, best_height, best_width, best_rect_count


def binom(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


if __name__ == '__main__':
    n = 2000000
    threshold = 3  # 2
    print(find_optimal_area(n, threshold))
