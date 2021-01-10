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


def coin_sum(val):
    possible_values = np.array([1, 2, 5, 10, 20, 50, 100, 200])
    poss_sum = 0
    for i1 in range(val, 0, -possible_values[7]):
        for i2 in range(i1, 0, -possible_values[6]):
            for i3 in range(i2, 0, -possible_values[5]):
                for i4 in range(i3, 0, -possible_values[4]):
                    for i5 in range(i4, 0, -possible_values[3]):
                        for i6 in range(i5, 0, -possible_values[2]):
                            for i7 in range(i6, 0, -possible_values[1]):
                                # for i8 in range(i7, int(val / possible_values[0])):
                                # print(i1, i2, i3, i4, i5, i6, i7, i8)
                                poss_sum += 1
    return poss_sum


def coin_sum_dp(val):
    possible_values = np.array([1, 2, 5, 10, 20, 50, 100, 200])
    ways = np.zeros(val+1)
    ways[0] = 1
    for i in range(len(possible_values)):
        for j in range(possible_values[i], val+1):
            ways[j] += ways[j - possible_values[i]]
    return ways[val]


def counting_summation(n):
    ways = np.zeros(n+1)
    ways[0] = 1
    for i in range(1, n):
        for j in range(i, n+1):
            ways[j] += ways[j - i]
            # print(ways[j], j, i)
    return ways[n]


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
    # print('sum ways count:', counting_summation(5))
    # print('coin sum ways count:', coin_sum_dp(200))
    print('distinct_prime_factor:', distinct_prime_factor(2))

