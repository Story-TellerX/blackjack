from player import AbstractPlayer
from const import MESSAGE_HOW_START_STOP_GAME


if __name__ == "__main__":
    choice_to_pLay = 'y'
    while choice_to_pLay:
        print(MESSAGE_HOW_START_STOP_GAME)
        input_player_choice = str(input("Have you really wanted to play with me?: "))
        if input_player_choice.lower() == 'n':
            break
        else:
            player_human = AbstractPlayer()
            player_human.get_player_name()
            player_human.add_player()
            player_human.greeting_player()


