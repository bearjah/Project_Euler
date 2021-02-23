import numpy as np


def find_nth_prime_num(n):
    nth_prime = 0
    while(True):
        num = 2
        if n % i == 0:
            if check_prime(i):
                largest_prime = i
    return largest_prime


def check_prime(num):
    for i in range(2, int(np.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = 10001
    print(find_nth_prime_num(n))
