from const import (
    MESSAGE_ADD_PLAYER,
    MESSAGE_REJECT_ADDING_PLAYER,
    MESSAGE_ADD_PLAYER_RULES,
    MESSAGE_SELECT_TYPE_OF_PLAYER,
    MESSAGE_SELECT_PLAYER_TYPE_RULES,
    MESSAGE_REJECT_SELECT_PLAYER_HUMAN_TYPE,
    MESSAGE_ACCEPT_HUMAN_PLAYER,
)


class AbstractPlayer:

    def __init__(self):
        self.player_type = 0
        self.player_name = 'default_name'
        self.player_cards = {}

    def get_player_type(self):
        print(MESSAGE_SELECT_PLAYER_TYPE_RULES)
        player_choise_to_add_human = int(input(f"{MESSAGE_SELECT_TYPE_OF_PLAYER}: "))
        if player_choise_to_add_human == 1:
            print(MESSAGE_ACCEPT_HUMAN_PLAYER)
            self.player_type = 1
            return self.player_type
        elif player_choise_to_add_human == 2:
            print(MESSAGE_REJECT_SELECT_PLAYER_HUMAN_TYPE)
            self.player_type = 2
            return self.player_type
        else:
            raise ValueError

    def get_player_name(self):
        if self.player_name == 'default_name':
            name_input = str(input("How can I call you protein man: "))
            self.player_name = name_input
            return self.player_name
        else:
            raise TypeError

    def add_player(self):
        default_player_type = self.player_type
        print(MESSAGE_ADD_PLAYER_RULES)
        input_player_choise_to_add = str(input(f"{MESSAGE_ADD_PLAYER}: "))
        if input_player_choise_to_add.lower() == 'y':
            type_of_player = self.get_player_type()
            return type_of_player
        elif input_player_choise_to_add.lower() == 'n':
            print(MESSAGE_REJECT_ADDING_PLAYER)
            return default_player_type
        else:
            raise ValueError

    def greeting_player(self):
        return print("The game will show if you are worthy of such a name {}".format(self.player_name))


