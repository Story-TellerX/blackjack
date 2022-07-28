from abc import ABC
from typing import Optional, Union

from cards import Shuffle
from const import MESSAGE_ADD_PLAYER_RULES, MESSAGE_ADD_PLAYER, MESSAGE_REJECT_ADDING_PLAYER
from player import ComputerPlayer, HumanPlayer


class AbstractGame(ABC):

    def __init__(self):
        self.player_moves = {}
        self.players_scores = {}
        self.card_deck = {}


class GameControl(AbstractGame):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_player_name(player_hum: HumanPlayer) -> str:
        if player_hum.player_name == 'default_name':
            name_input = str(input("How can I call you protein man: "))
            player_hum.player_name = name_input
            return player_hum.player_name
        else:
            raise TypeError

    @staticmethod
    def set_player_comp_name(player_comp: ComputerPlayer, player_hum: HumanPlayer) -> None:
        player_comp.player_name = 'Blender'
        print('I`m gonna build my own thing party with blackjack and hook...')
        print("Just call me Blender")
        player_hum.greeting_player()

    def get_cards_deck(self) -> dict:
        cards_deck_one = Shuffle().randomizer_for_cards_in_deck()
        self.card_deck = cards_deck_one
        return self.card_deck

    def _get_cards_from_deck(self, object_in_list):
        cards = {}
        if len(object_in_list.player_cards) < 2:
            counter = 0
            for card in self.card_deck.keys():
                if counter < 2:
                    card_value = self.card_deck.get(card)
                    cards[card] = card_value
                    object_in_list.player_cards.update(cards)
                    counter += 1
        object_in_list.remove_cards_from_deck(self.card_deck)
        return self.card_deck

    def _get_start_cards(self, player_comp: ComputerPlayer, player_hum: HumanPlayer) -> dict:
        list_of_objects_from_params = [player_comp, player_hum]
        for object_in_list in list_of_objects_from_params:
            self._get_cards_from_deck(object_in_list)
        return self.card_deck

    def make_start_moves(self, player_hum: HumanPlayer, player_comp: ComputerPlayer) -> dict:
        print("My cards")
        self._get_start_cards(player_comp, player_hum)
        print(player_comp.player_cards)
        player_comp.get_player_score()
        print("These cards your")
        print(player_hum.player_cards)
        print(f'This is your score: {player_hum.get_player_score()}')
        return self.card_deck

    def get_next_card(self, player_hum: HumanPlayer) -> int:
        counter = 0
        while player_hum.ask_player_for_next_card(self.card_deck, counter):
            if player_hum.ask_player_for_next_card is False:
                break
            counter += 1
        player_hum.player_move = 2
        return player_hum.player_move

    def human_moves(self, player_hum: HumanPlayer) -> dict:
        if self.get_next_card(player_hum):
            player_hum.remove_cards_from_deck(self.card_deck)
        return self.card_deck

    @staticmethod
    def do_comp_need_a_make_move_in_general(player_hum: HumanPlayer):
        do_hum_have_over21 = player_hum.player_score
        if do_hum_have_over21 > 21:
            return False
        elif do_hum_have_over21 <= 21:
            return True

    def get_next_card_for_comp(self, player_hum: HumanPlayer, player_comp: ComputerPlayer) -> int:
        counter = 0
        while self.do_comp_need_a_make_move_in_general(player_hum) is True:
            if player_comp.check_for_score():
                if player_comp.make_decision_to_take_card() is True:
                    print("I will take one more card")
                    player_comp.select_one_next_card(self.card_deck, counter)
                    player_comp.get_player_score()
                    counter += 1
                elif player_comp.make_decision_to_take_card() is False:
                    print("It is enough for me, I`m stop")
                    break
            else:
                break
        player_comp.player_move = 2
        return player_comp.player_move

    def comp_moves(self, player_hum: HumanPlayer, player_comp: ComputerPlayer) -> dict:
        if player_hum.player_move == 2:
            self.get_next_card_for_comp(player_hum, player_comp)
            player_comp.remove_cards_from_deck(self.card_deck)
        return self.card_deck

    @staticmethod
    def how_is_the_winner(player_hum: HumanPlayer, player_comp: ComputerPlayer) -> Optional[bool]:
        human_score = player_hum.get_player_score()
        comp_score = player_comp.get_player_score()
        print(f'The final result: My score is: {comp_score} and your score is: {human_score}, so...')
        if comp_score > 21 and human_score > 21:
            return None
        elif human_score < comp_score <= 21:
            return False
        elif comp_score < human_score <= 21:
            return True
        elif comp_score == human_score:
            return None

