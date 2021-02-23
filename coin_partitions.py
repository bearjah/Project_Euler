from itertools import accumulate, repeat
from operator import itemgetter


def calc_p(acc, _):
    prev, prev_prev = acc
    return prev_prev, prev + prev_prev


def main():
    for x, p in enumerate(map(itemgetter(1), accumulate(repeat((1, 1)), calc_p))):
        print(x + 1, p)
        if x == 50:
            return


if __name__ == '__main__':
    main()
