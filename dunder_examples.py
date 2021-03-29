# example from the Python Data Model chapter of Fluent Python by Luciano Ramalho
# A Pythonic card deck implementing a few dunder methods.

import collections
from random import choice

# construct class here using namedtuple. namedtuple will build classes of objects
# that are just bundles of attributes with no custom methods, similar to a database record
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(f"Length of deck: {len(deck)}")

beer_card = Card('7', 'diamonds')
print(beer_card)

# the __getitem__ method provides the ability to read cards
print(deck[0])
print(deck[-1])

# print out random card using random.choice method. It will return a random card.
print(choice(deck))
print(choice(deck))
print(choice(deck))

# look at the top three cards from a brand new deck, and then pick Aces by
# starting at index 12 and skipping 13 cards at a time

print(deck[:3])
print(deck[12::13])

# We can also iterate through the deck by implementing the __getitem__ method
# any call of a dunder method usually is implicit. You don't have to worry about calling a dunder method yourself.
for card in deck:
    print(card)

# iterate through the deck in reverse
for card in reversed(deck):
    print(card)

# because collection has no __contains__ method, the in operator does a sequential scan.
# returns true or false depending on whether card is in deck
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

# We can also sort the deck by ranking cards, with aces being the highest.
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

print('\n')


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# with the spades_high function, we can list our deck in order of increasing rank
for card in sorted(deck, key=spades_high):
    print(card)

# if you need invoke a special method, it is usually better to call the related build-in function (e.g. len, iter, str).
# These built-ins call the corresponding special method.

