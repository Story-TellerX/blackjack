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
    def _ask_about_one_more_card(self):
        raise NotImplemented

    @abc.abstractmethod
    def make_next_moves(self):
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

    def _ask_about_one_more_card(self):
        i = 0
        while i < 1:
            human_input = str(input(f'{MESSAGE_TO_GET_CARD_STOP_GETTING}'))
            if human_input.lower() == 'n':
                return False
            elif human_input.lower() == 'y':
                i = 1
                return True
            else:
                print(INPUT_NOT_VALID)

    def make_next_moves(self, card_deck=None):
        print("Your move...")
        while True:
            if not self.check_player_score():
                print("SORRY THIS IS TOO MUCH")
                break
            if not self._ask_about_one_more_card():
                print(f"You are stopped and your score is: {self.player_score}")
                break
            self.get_new_card(card_deck)
            print(self.player_card)
            print(f'This is your new score: {self.player_score}')


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

    def _ask_about_one_more_card(self):
        if self.player_score <= 12:
            print("I will take one more card")
            return True
        elif 12 < self.player_score < 17:
            print("I will take one more card")
            return True
        elif self.player_score >= 17:
            return False

    def make_next_moves(self, card_deck=None):
        print("Now is my turn...")
        while True:
            if not self.check_player_score():
                print("OH NO, THIS IS TOO MUCH")
                break
            if not self._ask_about_one_more_card():
                print(f"I will stop and my score is: {self.player_score}")
                break
            self.get_new_card(card_deck)
            print(self.player_card)
            print(f'This is my score: {self.player_score}')
