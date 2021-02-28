import numpy as np
# from itertools import sort


def find_relatively_primes(n, primes) -> int:
    relatively_primes = [1]
    own_primes = []
    total_relatively_primes = []
    for p in primes:
        if n % p == 0:
            own_primes.append(p)
        else:
            relatively_primes.append(p)
    res = [(x * y) for x, y in zip(relatively_primes, relatively_primes) if x * y < n]
    [total_relatively_primes.append(x) for x in (relatively_primes+res) if x not in total_relatively_primes]
    # print(n, total_relatively_primes)
    return len(total_relatively_primes)

# def find_relatively_primes(n) -> int:
#     if is_prime(n):
#         # print(n, [i for i in range(1, n)])
#         return n - 1
#     relatively_primes = [1]
#     comb_of_relatively_primes = []
#     prime_factors = []
#     res = []
#     for i in range(2, n):
#         if is_prime(i):
#             if n % i == 0:
#                 prime_factors.append(i)
#             else:
#                 relatively_primes.append(i)
#         else:
#             for p in prime_factors:
#                 if i % p == 0:
#                     break
#                 for k in relatively_primes:
#                     if i % k == 0:
#                         comb_of_relatively_primes.append(i)
#     total_factors = relatively_primes + comb_of_relatively_primes
#     [res.append(x) for x in total_factors if x not in res]
#     # print(n, sorted(res))
#     return len(res)


def is_prime(n) -> bool:
    for i in range(2, int(np.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    max_div_val = 0
    prime_list = []
    max_i = 0
    for i in range(2, 1000000):
        if is_prime(i):
            prime_list.append(i)
            phi = i-1
        else:
            phi = find_relatively_primes(i, prime_list)
        div = i/phi
        if div > max_div_val:
            max_div_val = div
            max_i = i
    print(max_div_val, max_i)
