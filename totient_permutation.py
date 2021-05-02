import math


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


def SieveOfEratosthenes(n) -> list:
    prime = [True for i in range(n)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime


def get_totient_minimum_permutation() -> list:
    min_ratio = 999
    index_min = None
    phi_min = None
    limit = 10 ** 7
    sqrt_limit = 2 * math.floor(math.sqrt(limit))
    primes = SieveOfEratosthenes(sqrt_limit)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] and primes[j]:
                n = i * j
                if n > limit:
                    break
                phi = (i - 1) * (j - 1)
                ratio = float(n) / phi
                if ratio < min_ratio and is_permutation(n, phi):
                    min_ratio = ratio
                    index_min = n
                    phi_min = int(phi)
                    print(index_min, phi_min, min_ratio)
    return [index_min, phi_min, min_ratio]


if __name__ == '__main__':
    print(get_totient_minimum_permutation())
