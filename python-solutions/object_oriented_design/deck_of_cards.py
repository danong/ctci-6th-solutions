import random
from itertools import product


class Card:
    """A card

    Examples:
        Card(1, 0) -> Ace of Diamonds
        Card(6, 3) -> 6 of Spades
        Card(13, 1) -> King of Clubs
        Card(10, 2) -> Jack of Hearts
    """
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
              'Queen', 'King']
    suites = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    def __init__(self, value: int, suite: int) -> None:
        """Construct a card

        Args:
            value: number between 1 and 13('A': 1, 'J': 10, etc.)
            suite: number between 0 and 3
        """
        self.value = value
        self.suite = suite

    def __str__(self):
        return '{} of {}'.format(self.values[self.value - 1],
                                 self.suites[self.suite])


class Deck:
    """A standard 52 card deck

    It is initialized with all 52 cards

    """

    def __init__(self):
        self.card_list = []
        self.reset()

    def reset(self):
        self.card_list = [Card(suite, value) for value, suite in
                          product(range(0, 4), range(1, 14))]

    def shuffle(self):
        random.shuffle(self.card_list)

    def deal(self, n=1):
        for _ in range(0, n):
            yield self.card_list.pop()

    def random_insert(self, card):
        random_idx = random.randrange(len(self.card_list) + 1)
        self.card_list.insert(random_idx, card)


if __name__ == '__main__':
    print(Card(1, 0))
    for card in Deck().card_list:
        print(card)
