class Card:
    # hold a card, location, and see if they matched or not
    def __init__(self, word, location):
        self.card = word
        self.location = location
        self.matched = False

    # __eq__
    def __eq__(self, other):
        return self.card == other.card

    # __str__
    def __str__(self):
        return self.card


if __name__ == "__main__":
    card1 = Card("egg", "A1")
    card2 = Card("egg", "B1")
    card3 = Card("hut", "C1")

    print(card1 == card2)
    print(card1 == card3)
    print(card1)
