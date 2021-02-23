import numpy as np


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


if __name__ == '__main__':
    n = 600851475143
    print(find_largest_prime_factor(n))
