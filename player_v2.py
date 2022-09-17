import abc
from abc import ABC


class AbstractPlayer(abc.ABC):

    @abc.abstractmethod
    def get_new_card(self):
        raise NotImplemented

    # @abc.abstractmethod
    # def remove_card_from_desk(self):
    #     raise NotImplemented

    @abc.abstractmethod
    def get_player_score(self):
        raise NotImplemented

    @abc.abstractmethod
    def check_player_score(self):
        raise NotImplemented

    @abc.abstractmethod
    def ask_about_one_more_card(self):
        raise NotImplemented


class HumanPLayer(AbstractPlayer, ABC):
    player_name: str

    def __init__(self, player_name):
        self.player_name = player_name
        self.player_card = []
        self.player_score = int

    def get_new_card(self, card_deck: list) -> list:
        new_card_from_deck = card_deck[0]
        self.player_card.append(new_card_from_deck)
        card_deck.remove(new_card_from_deck)
        return card_deck

    def get_player_score(self) -> int:
        card_score = []
        for card_name in self.player_card:




