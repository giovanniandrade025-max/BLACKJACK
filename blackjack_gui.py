import tkinter as tk
from blackjack import Blackjack, Action, Outcome, Phase


class HandView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bd=2, relief="groove", padx=10, pady=8)

        self.title = tk.Label(self, font=("TkDefaultFont", 12, "bold"))
        self.title.pack(anchor="w")

        self._cards = tk.Frame(self, width=450, height=80)
        self._cards.pack_propagate(False)
        self._cards.pack(anchor="w", pady=(6, 0))

        self._card_labels: list[tk.Label] = []

    def show(self, participant) -> None:
        self.title.config(text=f"{participant.name} — {participant.points} pontos")

        for lbl in self._cards.winfo_children():
            lbl.destroy()

        for card in participant.hand:
            tk.Label(self._cards, text=str(card),
                     font=("TkDefaultFont", 24)).pack(side="left", padx=2)


class BlackjackApp(tk.Tk):
    DEALER_ACTIONS = {
        Phase.DEALING:     (Action.DEALER_DEAL,   "Distribuindo cartas..."),
        Phase.CARD_REVEAL: (Action.DEALER_REVEAL, "Revelando a carta do dealer..."),
        Phase.DEALER_TURN: (Action.DEALER_PLAY,   "Vez do dealer..."),
    }

    OUTCOME_MESSAGES = {
        Outcome.PLAYER_WINS: "Você venceu!",
        Outcome.DEALER_WINS: "O dealer venceu.",
        Outcome.PUSH:        "Empate.",
    }
    
    STATUS_MESSAGES = {Phase.PLAYER_TURN: "Sua vez. Pedir ou Parar?"}
    DEALER_DELAY_MS = 700

    def __init__(self):
        super().__init__()
        self.title("Blackjack")
        self.resizable(False, False)

        self._game = Blackjack()
        self._after_id: str | None = None

        self._dealer_view = HandView(self)
        self._dealer_view.pack(fill="x", padx=10, pady=5)

        self._player_view = HandView(self)
        self._player_view.pack(fill="x", padx=10, pady=5)

        self._status = tk.Label(self, font=("TkDefaultFont", 11))
        self._status.pack(pady=10)

        bar = tk.Frame(self)
        bar.pack(pady=10)
        
        self._hit_button   = tk.Button(bar, text="Pedir",        width=10, command=self._hit)
        self._stand_button = tk.Button(bar, text="Parar",        width=10, command=self._stand)
        self._new_button   = tk.Button(bar, text="Nova partida", width=12, command=self._new_game)
        
        self._hit_button.pack(side="left", padx=5)
        self._stand_button.pack(side="left", padx=5)
        self._new_button.pack(side="left", padx=5)

        self._update_view()
        self._auto_step()

    def _new_game(self) -> None:
        if self._after_id is not None:
            self.after_cancel(self._after_id)
            self._after_id = None
        self._game = Blackjack()
        self._update_view()
        self._auto_step()

    def _hit(self) -> None:
        self._game.dispatch(Action.PLAYER_HIT)
        self._update_view()

    def _stand(self) -> None:
        self._game.dispatch(Action.PLAYER_STAND)
        self._update_view()
        self._auto_step()

    def _auto_step(self) -> None:
        if self._game.phase in self.DEALER_ACTIONS:
            self._after_id = self.after(self.DEALER_DELAY_MS, self._advance)

    def _advance(self) -> None:
        self._after_id = None

        if self._game.phase not in self.DEALER_ACTIONS:
            return
        
        action = self.DEALER_ACTIONS[self._game.phase][0]
        self._game.dispatch(action)
        self._update_view()
        self._auto_step()

    def _update_view(self) -> None:
        self._dealer_view.show(self._game.dealer)
        self._player_view.show(self._game.player)
        
        phase = self._game.phase

        if phase == Phase.FINISHED:
            self._status.config(text=self.OUTCOME_MESSAGES[self._game.outcome()])
        elif phase in self.DEALER_ACTIONS:
            self._status.config(text=self.DEALER_ACTIONS[phase][1])
        else:
            self._status.config(text=self.STATUS_MESSAGES.get(phase, ""))

        player_turn = phase == Phase.PLAYER_TURN
        self._hit_button.config(state="normal" if player_turn else "disabled")
        self._stand_button.config(state="normal" if player_turn else "disabled")
        self._new_button.config(state="normal" if phase == Phase.FINISHED else "disabled")

def main() -> None:
    app = BlackjackApp()
    app.mainloop()

if __name__ == "__main__":
    main()