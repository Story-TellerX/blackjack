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
    def get_start_cards(self):
        pass

    @abc.abstractmethod
    def get_next_card(self):
        pass

    @abc.abstractmethod
    def get_player_score(self):
        pass

    @abc.abstractmethod
    def greeting_player(self):
        pass


class ComputerPlayer(AbstractPlayer):

    def __init__(self):
        super().__init__()

    def _get_card_as_dict(self, cards):
        card_as_dict = {x: y for x, y in cards}
        return card_as_dict

    def remove_cards_from_deck(self, card_deck):
        if self.player_cards != {}:
            for i in self.player_cards.keys():
                try:
                    card_deck.pop(i)
                except KeyError:
                    pass
        return card_deck

    def get_start_cards(self, card_deck, player_comp):
        cards = []
        if len(self.player_cards) < 2:
            counter = 0
            for card in card_deck.items():
                if counter < 1:
                    cards.append(card)
                    counter += 1
            self._get_card_as_dict(cards)
            self.player_cards.update(self._get_card_as_dict(cards))
            player_comp.remove_cards_from_deck(card_deck)
        return card_deck


class HumanPlayer(AbstractPlayer):

    def __init__(self):
        super().__init__()

    def greeting_player(self):
        return print("The game will show if you are worthy of such a name {}".format(self.player_name))

    def remove_cards_from_deck(self, card_deck):
        if self.player_cards != {}:
            for i in self.player_cards.keys():
                try:
                    card_deck.pop(i)
                except KeyError:
                    pass
        return card_deck

    def get_start_cards(self, card_deck, player_hum):
        cards = {}
        if len(self.player_cards) < 2:
            counter = 0
            for card in card_deck.keys():
                if counter < 1:
                    card_value = card_deck.get(card)
                    cards[card] = card_value
                    counter += 1
        self.player_cards.update(cards)
        player_hum.remove_cards_from_deck(card_deck)
        return card_deck

    def get_player_score(self) -> int:
        players_cards = self.player_cards
        cards_score = []
        for card in players_cards.values():
            cards_score.append(card)
        self.player_score = sum(cards_score)
        return self.player_score

    def _check_for_score(self):
        if self.player_score <= 21:
            return True
        elif self.player_score > 21:
            print("Sorry IS TOO MUCH")
            print("I knew you would lose. The human brain cannot compete with mine.")
            return False
        else:
            return None

    def _select_one_next_card(self, card_deck, counter):
        cards = {}
        cards_dict_keys = card_deck.keys()
        card_key = list(cards_dict_keys)[counter]
        card_value = card_deck.get(card_key)
        cards[card_key] = card_value
        self.player_cards.update(cards)
        print(self.player_cards)

    def _ask_player_for_next_card(self):
        player_input = str(input(MESSAGE_TO_GET_CARD_STOP_GETTING))
        if player_input.lower() == 'y':
            return True
        elif player_input.lower() == 'stop':
            print("you stopped and have: {}".format(self.player_score))
            return False
        elif player_input.lower() != 'y' and player_input.lower() != 'stop':
            print("Please use only y or stop")
        else:
            return None

    def get_next_card(self, card_deck):
        player_input = "y"
        while player_input == "y":
            counter = 0
            while self._ask_player_for_next_card() is True:
                self._select_one_next_card(card_deck, counter)
                self.get_player_score()
                print(f'Your score is: {self.player_score}')
                if self._check_for_score() is False:
                    break
                elif self._check_for_score():
                    counter += 1

            return card_deck
        self.player_move = 2
        return self.player_move
