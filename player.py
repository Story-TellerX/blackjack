from abc import ABC
from typing import Optional, Dict, Any

from const import (
    #     MESSAGE_ADD_PLAYER,
    #     MESSAGE_REJECT_ADDING_PLAYER,
    #     MESSAGE_ADD_PLAYER_RULES,
    #     MESSAGE_SELECT_TYPE_OF_PLAYER,
    #     MESSAGE_SELECT_PLAYER_TYPE_RULES,
    #     MESSAGE_REJECT_SELECT_PLAYER_HUMAN_TYPE,
    #     MESSAGE_ACCEPT_HUMAN_PLAYER,
    MESSAGE_TO_GET_CARD_STOP_GETTING
)
import abc


class AbstractPlayer:

    def __init__(self):
        self.player_type = 0
        self.player_name = 'default_name'
        self.player_cards = {}
        self.player_score = 0
        self.player_move = 0

    @abc.abstractmethod
    def get_next_card(self):
        pass

    @abc.abstractmethod
    def get_player_score(self):
        pass

    @abc.abstractmethod
    def greeting_player(self):
        pass


class ComputerPlayer(AbstractPlayer, ABC):

    def __init__(self):
        super().__init__()
        self.player_human_score = 0

    def remove_cards_from_deck(self, card_deck: dict) -> dict:
        if self.player_cards != {}:
            for i in self.player_cards.keys():
                try:
                    card_deck.pop(i)
                except KeyError:
                    pass
        return card_deck

    def get_player_score(self) -> int:
        players_cards = self.player_cards
        cards_score = []
        for card in players_cards.values():
            cards_score.append(card)
        self.player_score = sum(cards_score)
        print(f'It is my score: {self.player_score}')
        return self.player_score

    def check_for_score(self) -> Optional[bool]:
        if self.player_score <= 21:
            return True
        elif self.player_score > 21:
            print("Oh-hh IS TOO MUCH")
            return False
        else:
            return None

    def select_one_next_card(self, card_deck: dict, counter: int) -> int:
        cards = {}
        cards_dict_keys = card_deck.keys()
        card_key = list(cards_dict_keys)[counter]
        card_value = card_deck.get(card_key)
        cards[card_key] = card_value
        self.player_cards.update(cards)
        print(self.player_cards)
        return counter

    def make_decision_to_take_card(self):
        self.get_player_score()
        if self.player_score <= 12:
            return True
        elif 12 < self.player_score < 17:
            return True
        elif self.player_score >= 17:
            return False


class HumanPlayer(AbstractPlayer, ABC):

    def __init__(self):
        super().__init__()

    def greeting_player(self) -> None:
        return print("The game will show if you are worthy of such a name {}".format(self.player_name))

    def remove_cards_from_deck(self, card_deck: dict) -> dict:
        if self.player_cards != {}:
            for i in self.player_cards.keys():
                try:
                    card_deck.pop(i)
                except KeyError:
                    pass
        return card_deck

    def get_player_score(self) -> int:
        players_cards = self.player_cards
        cards_score = []
        for card in players_cards.values():
            cards_score.append(card)
        self.player_score = sum(cards_score)
        return self.player_score

    def _check_for_score(self) -> Optional[bool]:
        if self.player_score <= 21:
            return True
        elif self.player_score > 21:
            print("Sorry IS TOO MUCH")
            print("I knew you would lose. The human brain cannot compete with mine.")
            return False
        else:
            return None

    def _select_one_next_card(self, card_deck: dict, counter: int) -> None:
        cards = {}
        cards_dict_keys = card_deck.keys()
        card_key = list(cards_dict_keys)[counter]
        card_value = card_deck.get(card_key)
        cards[card_key] = card_value
        self.player_cards.update(cards)
        print(self.player_cards)

    def ask_player_for_next_card(self, card_deck: dict,  counter: int) -> Optional[bool]:
        player_input = str(input(MESSAGE_TO_GET_CARD_STOP_GETTING))

        if player_input.lower() == 'y':
            self._select_one_next_card(card_deck, counter)
            self.get_player_score()
            if self._check_for_score() is False:
                self.get_player_score()
                print(f'Your score is: {self.player_score}')
                return False
            elif self._check_for_score():
                self.get_player_score()
                print(f'Your score is: {self.player_score}')
                counter += 1
                return True
        elif player_input.lower() == 'stop':
            self.get_player_score()
            print(f'Your stopped and your score is: {self.player_score}')
            return False
        elif player_input.lower() != 'y' and player_input.lower() != 'stop':
            print("Please use only y or stop")
        else:
            return None
