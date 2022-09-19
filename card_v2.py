import random

from const import CARD_DECK


class CardDeckShuffle:

    def __init__(self):
        self.card_decks_number = 1
        self.card_deck_raw = CARD_DECK
        self.card_deck_list = None

    def _create_a_list_of_cards(self) -> None:
        cards_name_dict_list = self.card_deck_raw.keys()
        cards_name_list = list(cards_name_dict_list)
        self.card_deck_list = cards_name_list

    def create_a_card_deck_for_game(self) -> list:
        self._create_a_list_of_cards()
        temp_list_for_shuffle = self.card_deck_list
        random.shuffle(temp_list_for_shuffle)
        self.card_deck_list = temp_list_for_shuffle
        card_deck = self.card_deck_list
        return card_deck
