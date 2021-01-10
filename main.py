import numpy as np
import scipy as sc
import math


def multiply_of_2_nums(num1, num2, n):
    sum_result = 0
    for i in range(min(num1, num2), n):
        if (i % num1) == 0 or (i % num2) == 0:
            sum_result += i
            print(i)
    return sum_result


def find_largest_prime_factor(n):
    largest_prime = 2
    for i in range(2, int(np.sqrt(n) + 1)):
        if n % i == 0:
            if check_prime(i):
                largest_prime = i
    return largest_prime


def check_prime(num):
    for i in range(2, int(np.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


# 85
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

    return "area = ", best_area, best_height, best_width, best_rect_count


def binom(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


def counting_summation(n):
    if n <= 2:
        print('returned(n==2):1')
        return 1
    a = n - 1
    b = n % a
    print(a, b, n)
    return counting_summation(a) + counting_summation(b)

    # for b in range(1, int(n/2+1)):  # int(n/2+1)):
    #     a = n - b
    #     print(a, b, n)
    #     count += counting_summation(a) + counting_summation(b)
    # return count


# n = 5: (6 options)
# 4 + 1 *
# 3 + 2
# 3 + 1 + 1 *
# 2 + 2 + 1
# 2 + 1 + 1 + 1 *
# 1 + 1 + 1 + 1 + 1 *


if __name__ == '__main__':
    # num1 = 3
    # num2 = 5
    # n = 1000
    # print(multiply_of_2_nums(num1, num2, n))
    # n = 600851475143
    # print(find_largest_prime_factor(n))
    # n = 2000000
    # # n = 18
    # threshold = 3 # 2
    # print(find_optimal_area(n, threshold))
    print('sum ways result:', counting_summation(5))

