import random

CARD_DECK = {
    "2-clubs": 2,
    "3-clubs": 3,
    "4-clubs": 4,
    "5-clubs": 5,
    "6-clubs": 6,
    "7-clubs": 7,
    "8-clubs": 8,
    "9-clubs": 9,
    "10-clubs": 10,
    "J-clubs": 10,
    "Lady-clubs": 10,
    "King-clubs": 10,
    "Ace-clubs": 10,
    "2-hearts": 2,
    "3-hearts": 3,
    "4-hearts": 4,
    "5-hearts": 5,
    "6-hearts": 6,
    "7-hearts": 7,
    "8-hearts": 8,
    "9-hearts": 9,
    "10-hearts": 10,
    "J-hearts": 10,
    "Lady-hearts": 10,
    "King-hearts": 10,
    "Ace-hearts": 10,
    "2-diamonds": 2,
    "3-diamonds": 3,
    "4-diamonds": 4,
    "5-diamonds": 5,
    "6-diamonds": 6,
    "7-diamonds": 7,
    "8-diamonds": 8,
    "9-diamonds": 9,
    "10-diamonds": 10,
    "J-diamonds": 10,
    "Lady-diamonds": 10,
    "King-diamonds": 10,
    "Ace-diamonds": 10,
    "2-spades": 2,
    "3-spades": 3,
    "4-spades": 4,
    "5-spades": 5,
    "6-spades": 6,
    "7-spades": 7,
    "8-spades": 8,
    "9-spades": 9,
    "10-spades": 10,
    "J-spades": 10,
    "Lady-spades": 10,
    "King-spades": 10,
    "Ace-spades": 10,
}


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
