import random


class CardDeck:

    def __init__(self):
        self.card_decks_number = 1
        self.clubs = {}
        self.hearts = {}
        self.diamonds = {}
        self.spades = {}

    def _create_clubs(self) -> dict:
        self.clubs = {
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
            "Ace-clubs": 10
        }
        return self.clubs

    def _create_hearts(self) -> dict:
        self.hearts = {
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
            "Ace-hearts": 10
        }
        return self.hearts

    def _create_diamonds(self) -> dict:
        self.diamonds = {
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
            "Ace-diamonds": 10
        }
        return self.diamonds

    def _create_spades(self) -> dict:
        self.spades = {
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
            "Ace-spades": 10
        }
        return self.spades


class Shuffle(CardDeck):

    def __init__(self):
        super(CardDeck).__init__()

    def _create_list_card_deck(self) -> dict:
        card_deck_dict = {}
        clubs = self._create_clubs()
        card_deck_dict.update(clubs)
        hearts = self._create_hearts()
        card_deck_dict.update(hearts)
        diamonds = self._create_diamonds()
        card_deck_dict.update(diamonds)
        spades = self._create_spades()
        card_deck_dict.update(spades)
        return card_deck_dict

    def randomizer_for_cards_in_deck(self) -> dict:
        get_card_deck_dict = self._create_list_card_deck()
        b = list(get_card_deck_dict.items())
        random.shuffle(b)
        first_card_deck = dict(b)
        return first_card_deck

