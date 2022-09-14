from game import GameControl
from player import HumanPlayer, ComputerPlayer
from const import MESSAGE_HOW_START_STOP_GAME, INPUT_NOT_VALID


def check_for_start_game() -> bool:
    i = 0
    while i < 1:
        input_player_choice = str(input("Have you really wanted to play with me?: "))
        if input_player_choice.lower() == 'n':
            return False
        elif input_player_choice.lower() == 'y':
            i = 1
            return True
        else:
            print(INPUT_NOT_VALID)


def how_is_the_winner(game_control: GameControl, player_hum: HumanPlayer, player_comp: ComputerPlayer) -> None:
    results_of_game = game_control.how_is_the_winner(player_hum, player_comp)
    if results_of_game is True:
        print("Oh no it is impossible - YOU ARE WINNER")
    elif results_of_game is False:
        print("I`m Blender most powerfully computer mind. I`M WINNER")
    elif results_of_game is None:
        print("no one winner here... Make one more round!")
    else:
        print("Something is wrong...")


def run_the_game():
    game_control = GameControl()
    player_hum = HumanPlayer()
    player_comp = ComputerPlayer()

    game_control.get_player_name(player_hum)
    game_control.set_player_comp_name(player_comp, player_hum)
    card_deck = game_control.get_cards_deck()

    game_control.make_start_moves(player_hum, player_comp)
    game_control.human_moves(player_hum)
    game_control.comp_moves(player_hum, player_comp)

    how_is_the_winner(game_control, player_hum, player_comp)
    # print(len(card_deck))


if __name__ == "__main__":
    while True:
        print(MESSAGE_HOW_START_STOP_GAME)
        if not check_for_start_game():
            break
        run_the_game()
