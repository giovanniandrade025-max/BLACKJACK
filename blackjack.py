from enum import Enum, auto
from player import Player, Dealer
from exceptions import InvalidActionError

class Phase(Enum):

    DEALING =  auto()
    PLAYER_TURN = auto()
    CARD_REVEAL = auto()
    DEALER_TURN = auto()
    FINISHED = auto()

class Action(Enum):

    DEALER_DEAL = auto()
    PLAYER_HIT = auto()
    PLAYER_STAND = auto()
    DEALER_REVEAL = auto()
    DEALER_PLAY = auto()

class Outcome(Enum):

    PLAYING = auto()
    PLAYER_WINS = auto()
    DEALER_WINS = auto()
    PUSH = auto()

class Blackjack:

    _DEALER_STANDS_ON: int = 17

    def __init__(self):
        self._player = Player("Jogador")
        self._dealer = Dealer("Dealer")
        self._phase = Phase.DEALING

    @property
    def player(self):
        return self._player

    @property
    def dealer(self):
        return self._dealer  

    @property
    def phase(self):
        return self._phase

    def dispatch(self, action: Action):
        match self._phase, action:
            case Phase.DEALING, Action.DEALER_DEAL:
                dealt = len(self._dealer.hand) + len(self._player.hand)
                match dealt:
                    case 0:
                        self._dealer.deal_to(self._dealer)
                    case 1:
                        self._dealer.deal_to(self._dealer, face_up = False)
                    case _:
                        self._dealer.deal_to(self._player)
                if dealt == 3:
                    self._phase = Phase.PLAYER_TURN

            case Phase.PLAYER_TURN, Action.PLAYER_HIT:
                self._player.hit(self._dealer)
                if self._player.is_busted:
                    self.phase = Phase.FINISHED

            case Phase.PLAYER_TURN, Action.PLAYER_STAND:
                self._phase = Phase.CARD_REVEAL

            case Phase.CARD_REVEAL, Action.DEALER_REVEAL:
                self._dealer.reveal_card()
                if self._dealer.hidden_points >= self._DEALER_STANDS_ON:
                    self._phase = Phase.FINISHED
                else:
                    self._phase = Phase.DEALER_TURN

            case Phase.DEALER_TURN, Action.DEALER_PLAY:
                self._dealer.draw()
                if self._dealer.hidden_points >= self._DEALER_STANDS_ON:
                    self._phase = Phase.FINISHED

            case _:
                raise InvalidActionError("Ação inválida")

    def outcome(self) -> Outcome:
        if self._phase != Phase.FINISHED:
            return Outcome.PLAYING

        if self._player.is_busted:
            return Outcome.DEALER_WINS

        if self._dealer.is_busted:
            return Outcome.PLAYER_WINS

        player_points = self._player.hidden_points
        dealer_points = self._dealer.hidden_points

        if player_points > dealer_points:
            return Outcome.PLAYER_WINS
        if player_points < dealer_points:
            return Outcome.DEALER_WINS
        return Outcome.PUSH