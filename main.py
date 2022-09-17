from const import MESSAGE_HOW_START_STOP_GAME, INPUT_NOT_VALID


def run_the_game():
    # game_control = GameControl()
    # player_hum = HumanPlayer()
    # player_comp = ComputerPlayer()
    #
    # game_control.get_player_name(player_hum)
    # game_control.set_player_comp_name(player_comp, player_hum)
    # card_deck = game_control.get_cards_deck()
    #
    # game_control.make_start_moves(player_hum, player_comp)
    # game_control.human_moves(player_hum)
    # game_control.comp_moves(player_hum, player_comp)
    #
    # how_is_the_winner(game_control, player_hum, player_comp)
    # print(len(card_deck))
    ...


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
