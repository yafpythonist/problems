#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------
# Реализуйте функцию best_hand, которая принимает на вход
# покерную "руку" (hand) из 7ми карт и возвращает лучшую
# (относительно значения, возвращаемого hand_rank)
# "руку" из 5ти карт. У каждой карты есть масть(suit) и
# ранг(rank)
# Масти: трефы(clubs, C), пики(spades, S), червы(hearts, H), бубны(diamonds, D)
# Ранги: 2, 3, 4, 5, 6, 7, 8, 9, 10 (ten, T), валет (jack, J), дама (queen, Q), король (king, K), туз (ace, A)
# Например: AS - туз пик (ace of spades), TH - дестяка черв (ten of hearts), 3C - тройка треф (three of clubs)

# Задание со *
# Реализуйте функцию best_wild_hand, которая принимает на вход
# покерную "руку" (hand) из 7ми карт и возвращает лучшую
# (относительно значения, возвращаемого hand_rank)
# "руку" из 5ти карт. Кроме прочего в данном варианте "рука"
# может включать джокера. Джокеры могут заменить карту любой
# масти и ранга того же цвета, в колоде два джокерва.
# Черный джокер '?B' может быть использован в качестве треф
# или пик любого ранга, красный джокер '?R' - в качестве черв и бубен
# любого ранга.

# Одна функция уже реализована, сигнатуры и описания других даны.
# Вам наверняка пригодится itertools
# Можно свободно определять свои функции и т.п.
# -----------------
from itertools import groupby, combinations, product

COMMONRANKS = "23456789TJQKA"
WCRANKS = "W"
WCSUITS = "W"
REDWCSUITS = "R"
BLACKWCSUITS = "B"
REDCOMMONSUITS = "HD"
BLACKCOMMONSUITS = "CS"


def is_wildcard(card):
    return True if any((wcsign in card for wcsign in WCRANKS + WCSUITS + REDWCSUITS + BLACKWCSUITS)) else False


def representable_cards(wildcard):
    rank, suit = wildcard
    if rank in WCRANKS:
        rank = COMMONRANKS
    if suit in BLACKWCSUITS:
        suit = BLACKCOMMONSUITS
    elif suit in REDWCSUITS:
        suit = REDCOMMONSUITS
    elif suit in WCSUITS:
        suit = REDCOMMONSUITS + BLACKCOMMONSUITS
    return (f"{r}{s}" for r in rank for s in suit)


def hand_rank(hand):
    """Возвращает значение определяющее ранг 'руки'"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    """Возвращает список рангов (его числовой эквивалент),
    отсортированный от большего к меньшему"""

    return sorted((COMMONRANKS.index(rank) for rank, suit in hand))[::-1]


def flush(hand):
    """Возвращает True, если все карты одной масти"""
    return True if len(set((suit for rank, suit in hand))) == 1 else False


def straight(ranks):
    """Возвращает True, если отсортированные ранги формируют последовательность 5ти,
    где у 5ти карт ранги идут по порядку (стрит)

    !!! Не все то, у чего сумма совпадает с суммой арифметической прогрессии есть арифметическая прогрессия
    """
    return all((ranks[i - 1] - 1 == ranks[i] for i in range(1, len(ranks)))) or ranks == card_ranks(
        "AW 2W 3W 4W 5W".split())


def kind(n, ranks):
    """Возвращает первый ранг, который n раз встречается в данной руке.
    Возвращает None, если ничего не найдено"""
    for rank, group in groupby(ranks):
        if len(tuple(group)) == n:
            return rank
    return None


def two_pair(ranks):
    """Если есть две пары, то возврщает два соответствующих ранга,
    иначе возвращает None"""
    p1 = kind(2, ranks)
    p2 = kind(2, ranks[::-1])
    if p1 and p2 != p1:
        return p1, p2
    return None


def best_hand(hand):
    """Из "руки" в 7 карт возвращает лучшую "руку" в 5 карт """
    return max(combinations(hand, 5), key=hand_rank)


def best_wild_hand(hand):
    """best_hand но с джокерами"""
    common_cards = tuple((card for card in hand if not is_wildcard(card)))
    wcrs = ((rc for rc in representable_cards(card) if rc not in common_cards) for card in hand if is_wildcard(card))
    best_hands = (best_hand(common_cards + tuple(wcc)) for wcc in product(*wcrs))
    return max(best_hands, key=hand_rank)


def test_best_hand():
    print("test_best_hand...")
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])

    print('OK')


def test_best_wild_hand():
    print("test_best_wild_hand...")
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C WB".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C WR WB".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    print('OK')


if __name__ == '__main__':
    test_best_hand()
    test_best_wild_hand()
