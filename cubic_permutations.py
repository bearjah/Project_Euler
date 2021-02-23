from itertools import permutations, accumulate, repeat, count, takewhile
from collections import Counter
from math import pow


def cubic_permutations_inefficient(x: int):
    """
    Suboptimal implementation, computing all of the permutations is too expensive.
    """
    perms = set(map(lambda p: int(''.join(p)), permutations(str(x))))
    min_perm = min(perms)
    max_perm = max(perms)
    min_cubic_root = round(pow(min_perm, 1/3))
    r = min_cubic_root
    print('start scan')
    while True:
        cube = r * r * r
        if cube > max_perm:
            break
        if cube in perms:
            yield r, cube
        r += 1


def exp2():
    return accumulate(repeat(2), lambda e, _: 2 * e)


def cube(y):
    return y * y * y


def is_perm(a, b):
    return Counter(str(a)) == Counter(str(b))


def cubic_permutations(x):
    min_perm = int(''.join(sorted(str(x))))
    max_perm = int(''.join(sorted(str(x), reverse=True)))
    r = round(pow(min_perm, 1/3))
    cubes = takewhile(lambda c: c <= max_perm, map(cube, count(r)))
    return filter(lambda c: is_perm(x, c), cubes)


def main():
    perms_seen = set()
    for x, c in zip(count(2), map(cube, count(2))):
        num_permutations = sum(1 for _ in cubic_permutations(c))
        print(x, '->', c, '->', num_permutations)
        if num_permutations not in perms_seen:
            # print(x, '->', x * x * x, '->', num_permutations)
            perms_seen.add(num_permutations)
        if num_permutations == 5:
            break


if __name__ == '__main__':
    main()
