from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [ Card(inner,outer) for inner in values for outer in suits]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"
    #
    # # FOR ITERATORS
    def __iter__(self):
        return iter(self.cards)

    # FOR GENERATORS:
    # def __iter__(self):
    #     for card in self.cards:
    #         yield card

    def _deal(self, removeno):
        remaining = self.count()
        if remaining>0:
            actual = min([remaining,removeno])
            cards = self.cards[-actual:]
            self.cards = self.cards[:-actual]
            return cards
        else:
            raise ValueError("No cards left")

    def shuffle(self):
        if self.count() == 52 :
            shuffle(self.cards)
        else:
            raise ValueError("No cards left")

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
print('Remaining:', d.count())
hand = d.deal_hand(45)
print('Remaining:', d.count())

# Loop through the Deck object direcly as __iter__ is defined to return an Iterator object of the cards list
for card in d:
    print(card)

# card2 = d.deal_card()
# print(card2)
# print('Remaining:', d.count())
# card2 = d.deal_card()
# print('Remaining:', d.count())
