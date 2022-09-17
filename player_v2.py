import abc
from abc import ABC
from card_v2 import CARD_DECK
from const import MESSAGE_TO_GET_CARD_STOP_GETTING, INPUT_NOT_VALID


class AbstractPlayer(abc.ABC):

    @abc.abstractmethod
    def get_new_card(self):
        raise NotImplemented

    @abc.abstractmethod
    def _get_player_score(self):
        raise NotImplemented

    @abc.abstractmethod
    def check_player_score(self):
        raise NotImplemented

    @abc.abstractmethod
    def ask_about_one_more_card(self):
        raise NotImplemented


class HumanPlayer(AbstractPlayer, ABC):

    def __init__(self):
        self.player_name = str
        self.player_card = []
        self.player_score = 0

    def get_new_card(self, card_deck=None) -> list:
        new_card_from_deck = card_deck[0]
        self.player_card.append(new_card_from_deck)
        card_deck.remove(new_card_from_deck)
        self._get_player_score()
        return card_deck

    def _get_player_score(self, card_deck_with_value=CARD_DECK) -> int:
        card_score = []
        for card_name in self.player_card:
            card_value = card_deck_with_value[card_name]
            card_score.append(card_value)
        self.player_score = sum(card_score)
        return self.player_score

    def check_player_score(self):
        if self.player_score <= 21:
            return True
        else:
            return False

    def ask_about_one_more_card(self):
        human_input = str(input(f'{MESSAGE_TO_GET_CARD_STOP_GETTING}'))
        if human_input.lower() == 'n':
            return False
        elif human_input.lower() == 'y':
            print("You take new card")
            return True
        else:
            print(INPUT_NOT_VALID)


class ComputerPlayer(AbstractPlayer, ABC):

    def __init__(self):
        self.player_name = str
        self.player_card = []
        self.player_score = 0

    def get_new_card(self, card_deck=None) -> list:
        new_card_from_deck = card_deck[0]
        self.player_card.append(new_card_from_deck)
        card_deck.remove(new_card_from_deck)
        self._get_player_score()
        return card_deck

    def _get_player_score(self, card_deck_with_value=CARD_DECK) -> int:
        card_score = []
        for card_name in self.player_card:
            card_value = card_deck_with_value[card_name]
            card_score.append(card_value)
        self.player_score = sum(card_score)
        return self.player_score

    def check_player_score(self):
        if self.player_score <= 21:
            return True
        else:
            return False

    def ask_about_one_more_card(self):
        if self.player_score <= 12:
            print("I will take one more card")
            return True
        elif 12 < self.player_score < 17:
            print("I will take one more card")
            return True
        elif self.player_score >= 17:
            return False
