# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.

import sys

from collections import Counter
from operator import itemgetter, methodcaller
from itertools import groupby, zip_longest
from fn.iters import pairwise

card_types = '23456789TJQKA'
card_values = {c: i for i, c in enumerate(card_types)}
VALUE = 0
SUIT = 1
MAX_VALUE = 14


def card_score(card):
    return card_values[card[VALUE]] + 2


class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards, key=card_score)
        counts = Counter(card_score(card) for card in self.cards)
        self.most_common = counts.most_common()

    def is_flush(self):
        return len({card[SUIT] for card in self.cards}) == 1

    def is_straight(self):
        return all(card_score(b) - card_score(a) == 1 for a, b in pairwise(self.cards))

    def is_fullhouse(self):
        return len(self.most_common) == 2 and self.most_common[0][1] == 3

    def is_two_pairs(self):
        return len(self.most_common) == 3 and self.most_common[0][1] == 2

    def is_pair(self):
        return len(self.most_common) == 4 and self.most_common[0][1] == 2

    def is_triplet(self):
        return len(self.most_common) == 3 and self.most_common[0][1] == 3

    def is_quadruplet(self):
        return len(self.most_common) == 2 and self.most_common[0][1] == 4

    def score(self):
        self_is_flush = self.is_flush()
        self_is_straight = self.is_straight()
        if self_is_flush and self_is_straight:
            return 10, card_score(self.cards[-1])
        if self.is_quadruplet():
            return 9, self.most_common[0][0]
        if self.is_fullhouse():
            return 8, self.most_common[0][0]
        if self_is_flush:
            return 7, card_score(self.cards[-1])
        if self_is_straight:
            return 6, card_score(self.cards[-1])
        if self.is_triplet():
            return 5, self.most_common[0][0]
        if self.is_two_pairs():
            return 4, [score for score, _ in self.most_common]
        if self.is_pair():
            return 3, self.most_common[0][0]
        return 2, card_score(self.cards[-1])


s = 0

with open(sys.argv[1]) as f:
    for l in f:
        cards = l.split()
        hand1, hand2 = cards[:5], cards[5:]
        # hand1, hand2 = ['3C', '3C', '6S', '2C', '2C'], ['2C', '2C', 'AC', '3C', '3S']
        hand1_score = Hand(hand1).score()
        hand2_score = Hand(hand2).score()
        print(hand1, hand1_score, hand2, hand2_score)
        if hand1_score > hand2_score:
            s += 1

print(s)