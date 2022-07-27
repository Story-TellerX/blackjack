from game import GameControl
from player import AbstractPlayer, HumanPlayer, ComputerPlayer
from const import MESSAGE_HOW_START_STOP_GAME


def check_for_start_game() -> bool:
    i = 0
    while i < 1:
        input_player_choice = str(input("Have you really wanted to play with me?: "))
        if input_player_choice.lower() == 'n':
            break
        elif input_player_choice.lower() != 'y' and input_player_choice.lower() != 'n':
            print("Please enter only Y or N")
            i = 0
        elif input_player_choice.lower() == 'y':
            i = 1
            return True
        else:
            raise ValueError


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
    print(len(card_deck))


if __name__ == "__main__":
    choice_to_pLay = 'y'
    while choice_to_pLay:
        print(MESSAGE_HOW_START_STOP_GAME)
        if check_for_start_game():
            run_the_game()
        else:
            break
