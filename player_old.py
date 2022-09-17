import abc

from const import (
    GREETING_PLAYER_TEXT,
    MESSAGE_TO_GET_CARD_STOP_GETTING,
    INPUT_NOT_VALID,
)


class AbstractPlayer:

    def __init__(self):
        self.player_type = 0
        self.player_name = 'default_name'
        self.player_cards = {}
        self.player_score = 0
        self.player_move = 0

    @abc.abstractmethod
    def get_next_card(self):
        raise NotImplemented

    @abc.abstractmethod
    def get_player_score(self):
        raise NotImplemented

    @abc.abstractmethod
    def greeting_player(self):
        raise NotImplemented


class ComputerPlayer(AbstractPlayer, abc.ABC):

    def __init__(self):
        super().__init__()
        self.player_human_score = 0

    def remove_cards_from_deck(self, card_deck: dict, last_received_card: str) -> dict:
        if self.player_cards:
            card_deck.pop(last_received_card)
            # for i in self.player_cards.keys():
            #     try:
            #         card_deck.pop(i)
            #     except KeyError:
            #         pass
        return card_deck

    def get_player_score(self) -> int:
        players_cards = self.player_cards
        cards_score = []
        for card in players_cards.values():
            cards_score.append(card)
        self.player_score = sum(cards_score)
        print(f'It is my score: {self.player_score}')
        return self.player_score

    def check_for_score(self) -> bool:
        if self.player_score <= 21:
            return True
        elif self.player_score > 21:
            print("Oh-hh IS TOO MUCH")
            return False
        else:
            print("Some strange score")

    def select_one_next_card(self, card_deck: dict, counter: int) -> int:
        cards = {}
        cards_dict_keys = card_deck.keys()
        card_key = list(cards_dict_keys)[counter]
        card_value = card_deck.get(card_key)
        cards[card_key] = card_value
        self.player_cards.update(cards)
        print(self.player_cards)
        return counter

    def make_decision_to_take_card(self) -> bool:
        if self.player_score <= 12:
            return True
        elif 12 < self.player_score < 17:
            return True
        elif self.player_score >= 17:
            return False


class HumanPlayer(AbstractPlayer, abc.ABC):

    def __init__(self):
        super().__init__()

    def greeting_player(self) -> None:
        return print(f'{GREETING_PLAYER_TEXT} - {self.player_name}')

    def remove_cards_from_deck(self, card_deck: dict, last_received_card: str) -> dict:
        if self.player_cards:
            card_deck.pop(last_received_card)
            # for i in self.player_cards.keys():
            #     try:
            #         card_deck.pop(i)
            #     except KeyError:
            #         pass
        return card_deck

    def get_player_score(self) -> int:
        players_cards = self.player_cards
        cards_score = []
        for card in players_cards.values():
            cards_score.append(card)
        self.player_score = sum(cards_score)
        return self.player_score

    def _check_for_score(self) -> bool:
        if self.player_score <= 21:
            return True
        elif self.player_score > 21:
            print("Sorry IS TOO MUCH")
            print("I knew you would lose. The human brain cannot compete with mine.")
            print(f'Your score is: {self.player_score}')
            return False
        else:
            print("Some strange score")

    def _select_one_next_card(self, card_deck: dict, counter: int) -> None:
        cards = {}
        cards_dict_keys = card_deck.keys()
        card_key = list(cards_dict_keys)[counter]
        card_value = card_deck.get(card_key)
        cards[card_key] = card_value
        self.player_cards.update(cards)
        print(self.player_cards)

    def ask_player_for_next_card(self, card_deck: dict, counter: int) -> bool:
        while True:
            if not self._check_for_score():
                break
            player_input = str(input(MESSAGE_TO_GET_CARD_STOP_GETTING))
            if not self._check_for_hum_answer_for_next_card(player_input, card_deck, counter):
                break
            return True

    def _check_for_hum_answer_for_next_card(self, player_input: str, card_deck: dict, counter: int) -> bool:
        if player_input.lower() == 'y':
            self._select_one_next_card(card_deck, counter)
            self.get_player_score()
            print(f"Your score is {self.player_score} now")
            return True
        elif player_input.lower() == 'n':
            self.get_player_score()
            print(f'Your stopped and your score is: {self.player_score}')
            return False
        else:
            print(INPUT_NOT_VALID)
            return True
