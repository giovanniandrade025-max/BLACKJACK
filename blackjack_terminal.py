from blackjack import Blackjack, Phase, Action, Outcome

DEALER_ACTIONS = {
    Phase.DEALING:  (Action.DEALER_DEAL, "Distribuindo cartas..."),
    Phase.CARD_REVEAL: (Action.DEALER_REVEAL, "Revelando carta do dealer..."),
    Phase.DEALER_TURN: (Action.DEALER_PLAY, "Vez do dealer..."),
}

OUTCOME_MESSAGES = {
    Outcome.PLAYER_WINS: "Você venceu!",
    Outcome.DEALER_WINS: "O dealer venceu!",
    Outcome.PUSH:       "Empate!",
}

STATUS_MESSAGES = {
    Phase.PLAYER_TURN: "Sua vez. Pressione [Enter] para pedir uma carta ou [P] para parar."
}

def print_game(game: Blackjack, msg: str = '') -> None:

    print()
    print("=" *42)
    print(f"{game.dealer.name}: {game.dealer.points} pontos")
    print("  " + "  ".join(str(c) for c in game.dealer.hand))
    print()
    print(f"{game.player.name}: {game.player.points} pontos")
    print("  " + "  ".join(str(c) for c in game.player.hand))
    print("-" *42)
    if msg:
        print(f"  {msg}")
    print("=" *42)

def play_round() -> None:
    game = Blackjack()

    while game.phase != Phase.FINISHED:
        if game.phase in DEALER_ACTIONS:
            action, msg = DEALER_ACTIONS[game.phase]
            print_game(game, msg)
            input("  Pressione [Enter] para continuar...")
            game.dispatch(action)
        else:
            print_game(game, STATUS_MESSAGES[game.phase])
            choice = input("  Pressione [Enter] para pedir uma carta ou [P] para parar: ").strip().lower()
            game.dispatch(Action.PLAYER_HIT if choice == "" else Action.PLAYER_STAND)

    print_game(game, OUTCOME_MESSAGES[game.outcome])

def main() -> None:
    print("Bem-vindo à mesa do Blackjack. Divirta-se!")
    while True:
        play_round()
        if input("Deseja jogar novamente? (S/N): ").strip().lower() != "s":
            break

if __name__ == "__main__":
    main()