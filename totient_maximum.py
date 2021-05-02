import numpy as np


def get_phi(n, primes) -> int:
    phi = n
    for p in primes:
        phi *= (1 - 1/p)
    # print(phi)
    return phi


def is_prime(n) -> bool:
    for i in range(2, int(np.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def get_prime_factors(n) -> list:
    primes = []
    for i in range(2, int(np.sqrt(n) + 1)):
        if n % i == 0 and is_prime(i):
            primes.append(i)
    return primes


def find_totient_maximum(n) -> float:
    max_div = 0
    max_index = None
    for i in range(2, n+1):
        if is_prime(i):
            phi = i-1
        else:
            primes = get_prime_factors(i)
            # print(i, primes)
            phi = get_phi(i, primes)
        div = i/phi
        if div > max_div:
            max_div = div
            max_index = i
        print(i, div)
    # print(prime_list)
    return max_index


if __name__ == '__main__':
    print(find_totient_maximum(10 ** 6))
