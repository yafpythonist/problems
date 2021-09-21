from collections import namedtuple, defaultdict
from itertools import product, combinations
from random import sample

import selenium.webdriver.common.actions.interaction


class Card:
    """
    Actual card, as we see them. Actual cards might be jokers.
    """
    WCSUITFACES = frozenset("W")
    REDWCSUITFACES = frozenset("R")
    BLACKWCSUITFACES = frozenset("B")
    WCRANKFACES = frozenset("W")
    SUITFACES = frozenset("CSHDBRW")
    RANKFACES = frozenset("23456789TJQKAW")
    WCREDSUITS = frozenset("HD")
    WCBLACKSUITS = frozenset("CS")

    def __init__(self, face):
        rank, suit = face
        if rank in self.RANKFACES and suit in self.SUITFACES:
            self.face = face
        else:
            raise ValueError("Wrong Cardface mnemonic")

    def get_face(self):
        return self.face

    def get_rankface(self):
        rank, _ = self.face
        return rank

    def get_suitface(self):
        _, suit = self.face
        return suit

    def __str__(self):
        return self.face

    def __repr__(self):
        return f"Card('{self.face}')"

    def get_representable_cards(self):
        if self.get_suitface() in self.WCSUITFACES:
            suits = self.SUITFACES - self.WCSUITFACES - self.REDWCSUITFACES - self.BLACKWCSUITFACES
        elif self.get_suitface() in self.REDWCSUITFACES:
            suits = self.WCREDSUITS
        elif self.get_suitface() in self.BLACKWCSUITFACES:
            suits = self.WCBLACKSUITS
        else:
            suits = (self.get_suitface(),)
        if self.get_rankface() in self.WCRANKFACES:
            ranks = self.RANKFACES - self.WCRANKFACES
        else:
            ranks = (self.get_rankface(),)
        return set((Card(''.join(rs)) for rs in product(ranks, suits)))

class Poker_hand:
    RANKVALUES = (None, ) + tuple("A23456789TJQKA")

    def __init__(self, cardset):
        self.cardset = cardset

    def major_straights(self):
        rankdict = defaultdict(set)
        for card in self.cardset:
            for rcard in card.get_representable_cards():
                if rcard not in self.cardset:
                    rankdict[rcard.get_rankface()].add(card)
        for i in range(len(Poker_hand.RANKVALUES)-1, 4, -1):
            ranksubset = []
            for j in range(i-4,i+1):
                if rankdict[Poker_hand.RANKVALUES[j]]:
                    ranksubset.append(tuple(rankdict[Poker_hand.RANKVALUES[j]]))
            msset = set(cus for cus in (frozenset(cs)for cs in tuple(product(*ranksubset))) if len(cus) == 5)
            if len(msset)>0:
                return True, Poker_hand.RANKVALUES[i], msset
        return False, None, None

    def major_flushes(self):
        suitdict = defaultdict(set)
        for card in self.cardset:
            for rcard in card.get_representable_cards():
                if rcard not in self.cardset:
                    suitdict[rcard.get_suitface()].add(card)


        flushsuits = dict((k, suitdict[k]) for k in suitdict if len(suitdict[k])>=5)

        maxscore = 0
        maxflushes = {}
        for suit, fcardset in flushsuits.items():
            suit_score, suit_cardset = Poker_hand.score_sum(fcardset)
            if suit_score > maxscore:
                maxflushes.clear()
                maxscore, maxflushes[suit] = suit_score, suit_cardset
            elif suit_score == maxscore:
                maxflushes[suit] = suit_cardset

        return len(flushsuits) > 0, maxflushes

    @staticmethod
    def score_sum(cardset):
        countset = set()
        score = 0
        for i in range(len(Poker_hand.RANKVALUES)-1, 1, -1):
            for card in cardset:
                if card not in countset:
                    rcardrankset = set((rc.get_rankface() for rc in card.get_representable_cards()))
                    if Poker_hand.RANKVALUES[i] in rcardrankset:
                        score += i
                        countset.add(card)
                        break
        return score, countset



c = set((Card(face) for face in "2S WR KD 3C 4C 5C WB WW".split()))
ph = Poker_hand(c)
#print(Poker_hand.score_sum(c))
print("ms", ph.major_straights())
print("mf", ph.major_flushes())