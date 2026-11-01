import enum
class Suit(enum.Enum):
    CLUBS = (1, "♣", 0x1F0D0)
    DIAMONDS = (2, "♦", 0x1F0C0)
    HEARTS = (3, "♥", 0x1F0B0)
    SPADES = (4, "♠", 0x1F0A0)

    def __init__(self, order: int, symbol: str, unicode_base: int):
        self.order = order
        self.symbol = symbol
        self.unicode_base = unicode_base

class Rank(enum.Enum):
    ACE = (1, "A")
    TWO = (2, "2")
    THREE = (3, "3")
    FOUR = (4, "4")
    FIVE = (5, "5")
    SIX = (6, "6")
    SEVEN = (7, "7")
    EIGHT = (8, "8")
    NINE = (9, "9")
    TEN = (10, "10")
    JACK = (11, "J")
    QUEEN = (12, "Q")
    KING = (13, "K")

    def __init__(self, number: int, label: str):
        self.number = number
        self.label = label

class Card:
    BACK_UNICODE: str = "🂠"

    def __init__(self, rank: 'Rank', suit: 'Suit', face_up: bool = True):
        self._rank = rank
        self._suit = suit
        self._is_face_up = face_up

    @property
    def rank(self) -> Rank:
        return self._rank

    @property
    def suit(self) -> Suit:
        return self._suit

    @property
    def is_face_up(self) -> bool:
        return self._is_face_up

    def flip(self):
        self._is_face_up = not self._is_face_up

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self._rank == other._rank and self._suit == other._suit

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        if self._suit == other._suit:
            return self._rank.number < other._rank.number
        return self._suit.order < other._suit.order

    def __hash__(self) -> int:
        return hash((self._rank, self._suit))

    def __repr__(self) -> str:
        return f"Card({self._rank.label}{self._suit.symbol})"

    def __str__(self) -> str:
        if not self._is_face_up:
            return self.BACK_UNICODE
        return chr(self._suit.unicode_base + self._rank.number)
        
