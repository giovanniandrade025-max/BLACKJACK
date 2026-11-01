import random
from abc import ABC, abstractmethod
from typing import Iterable, Iterator
from card import Card, Rank, Suit
from exceptions import EmptyStockError

class CardCollection(ABC):
    def __init__(self, cards: Iterable[Card] = ()):
        self._cards: list[Card] = list(cards)

    def __len__(self) -> int:
        return len(self._cards)

    @abstractmethod
    def __iter__(self) -> Iterator[Card]:
        pass


class Stock(CardCollection):

    def __init__(self):
        cards = [
            Card(rank, suit, face_up=False)
            for suit in Suit
            for rank in Rank
        ]
        super().__init__(cards)

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw(self) -> Card:
        if not self._cards:
            raise EmptyStockError("Não há cartas no baralho.")
        return self._cards.pop()

    def __iter__(self) -> Iterator[Card]:
        return reversed(self._cards)


class Hand(CardCollection):

    def add(self, card: Card) -> None:
        self._cards.append(card)

    def play(self, card: Card) -> Card:
        self._cards.remove(card)
        return card

    def __iter__(self) -> Iterator[Card]:
        return iter(self._cards)
