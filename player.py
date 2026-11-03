from card import Card, Rank
from card_collections import Hand, Stock


class Participant:

    def __init__(self, name: str):
        self._name = name
        self._hand = Hand()

    @property
    def name(self):
        return self._name

    @property
    def hand(self):
        return tuple(self._hand)

    @property
    def points(self):
        cards = [
            card for card in self._hand
            if card.is_face_up
        ]
        return self._compute_points(cards)

    @property
    def hidden_points(self):
        return self._compute_points(self._hand)

    @property
    def is_busted(self):
        return self.hidden_points > 21

    def receive(self, card: Card):
        self._hand.add(card)

    @staticmethod
    def _compute_points(cards):
        points = 0
        aces = 0

        for card in cards:
            if card.rank == Rank.ACE:
                points += 11
                aces += 1
            else:
                points += min(card.rank.number, 10)

        while points > 21 and aces > 0:
            points -= 10
            aces -= 1

        return points


class Player(Participant):

    def hit(self, dealer):
        return dealer.deal_to(self, face_up=True)


class Dealer(Participant):

    def __init__(self, name: str):
        super().__init__(name)
        self._stock = Stock()
        self._stock.shuffle()

    @property
    def stock(self):
        return self._stock

    def draw(self):
        return self._stock.draw()

    def deal_to(self, participant, face_up=True):
        card = self.draw()

        if card.is_face_up != face_up:
            card.flip()

        participant.receive(card)

        return card

    def reveal_card(self):
        for card in self._hand:
            if not card.is_face_up:
                card.flip()
