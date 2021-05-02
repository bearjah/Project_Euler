import numpy as np
import math


def get_primes2(low_limit, high_limit):
    prime_list = []
    for num in range(low_limit, high_limit):
        if num % 2 == 0:
            continue
        if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
            prime_list.append(num)
        # print(num)
    return prime_list


def get_primes(low_range, high_range):
    out = list()
    n = high_range - low_range
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p] and sieve[p] % 2 == 1:
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out


def is_prime(n) -> bool:
    for i in range(2, int(np.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def is_permutation(n, m) -> bool:
    str1 = [x for x in str(n)]
    str2 = [x for x in str(m)]
    if len(str1) != len(str2):
        return False
    a = sorted(str1)
    str1 = " ".join(a)
    b = sorted(str2)
    str2 = " ".join(b)
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


def get_prime_permutation(n_digits) -> list:
    prime_seq = []
    low_range, high_range = 10 ** (n_digits - 1), 10 ** n_digits
    prime_list = get_primes2(low_range, high_range)
    for i in range(0, len(prime_list)):
        for j in range(i+1, len(prime_list)):
            prime1 = prime_list[i]
            prime2 = prime_list[j]
            k = prime2 + prime2 - prime1
            if k < high_range and k in prime_list:
                if is_permutation(prime1, prime2) and is_permutation(k, prime1):
                    prime_seq.append([prime1, prime2, k])
    return prime_seq


if __name__ == '__main__':
    print(get_prime_permutation(n_digits=4))
