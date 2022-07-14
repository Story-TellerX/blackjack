from abc import ABC

from cards import Shuffle
from const import MESSAGE_ADD_PLAYER_RULES, MESSAGE_ADD_PLAYER, MESSAGE_REJECT_ADDING_PLAYER
from player import ComputerPlayer, HumanPlayer


class AbstractGame(ABC):

    def __init__(self):
        self.player_moves = {}
        self.players_scores = {}
        self.card_deck = {}

    def create_players_comp(self):
        player_comp = ComputerPlayer()
        player_comp.player_type = 1
        return player_comp

    def create_players_human(self):
        player_hum = HumanPlayer()
        player_hum.player_type = 2
        return player_hum


class GameControl(AbstractGame):

    def __init__(self):
        super().__init__()

    def create_players_comp(self):
        return super().create_players_comp()

    def create_players_human(self):
        return super().create_players_human()

    def get_player_name(self, player_hum):
        if player_hum.player_name == 'default_name':
            name_input = str(input("How can I call you protein man: "))
            player_hum.player_name = name_input
            return player_hum.player_name
        else:
            raise TypeError

    def set_player_comp_name(self, player_comp, player_hum):
        player_comp.player_name = 'Blender'
        print('I`m gonna build my own thing party with blackjack and hook...')
        print("Just call me Blender")
        player_hum.greeting_player()

    def get_cards_deck(self):
        cards_deck_one = Shuffle().randomizer_for_cards_in_deck()
        self.card_deck = cards_deck_one
        return self.card_deck

    @staticmethod
    def make_start_moves(player_hum, player_comp, card_deck):
        print("My cards")
        player_comp.get_start_cards(card_deck, player_comp)
        player_comp.get_start_cards(card_deck, player_comp)
        print(player_comp.player_cards)
        print("These cards your")
        player_hum.get_start_cards(card_deck, player_hum)
        player_hum.get_start_cards(card_deck, player_hum)
        print(player_hum.player_cards)
        return card_deck

    @staticmethod
    def human_moves(player_hum, player_comp, card_deck):
        if player_hum.get_next_card(card_deck):
            player_hum.remove_cards_from_deck(card_deck)
        if player_hum.player_move == 2:
            player_comp.get_next_card(card_deck)
        return card_deck

