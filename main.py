from const import MESSAGE_HOW_START_STOP_GAME, INPUT_NOT_VALID
from game_v2 import GameControl


def run_the_game():
    game_control = GameControl()

    game_control.get_players_name()
    game_control.get_card_deck()

    game_control.starts_moves_to_take_2_cards()
    game_control.get_next_human_moves()
    game_control.get_next_comp_moves()

    game_control.how_is_the_winner_message()


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


if __name__ == "__main__":
    while True:
        print(MESSAGE_HOW_START_STOP_GAME)
        if not check_for_start_game():
            break
        run_the_game()
