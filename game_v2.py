from card_v2 import CardDeckShuffle
from const import (
    WINNER_MESSAGE_FOR_COMP,
    GREETING_PLAYER_TEXT,
    COMP_NAME_INTRODUCTION,
    WINNER_MESSAGE_FOR_HUMAN,
    MESSAGE_FOR_DRAW,
)
from player_v2 import HumanPlayer, ComputerPlayer


class GameControl:

    def __init__(self):
        self.card_deck_class = CardDeckShuffle()
        self.player_human = HumanPlayer()
        self.player_comp = ComputerPlayer()
        self.card_deck = []

    def get_players_name(self) -> None:
        player_name_input = str(input("How can I call you protein man: "))
        print(f"{GREETING_PLAYER_TEXT} {player_name_input}")
        self.player_human.player_name = player_name_input
        self.player_comp.player_name = "Blender"
        print(f"{COMP_NAME_INTRODUCTION} {self.player_comp.player_name}")

    def get_card_deck(self) -> None:
        card_deck_for_play = CardDeckShuffle().create_a_card_deck_for_game()
        self.card_deck = card_deck_for_play

    def starts_moves_to_take_2_cards(self) -> None:
        print("Your cards:")
        self.player_human.get_new_card(self.card_deck)
        self.player_human.get_new_card(self.card_deck)
        print(self.player_human.player_card)
        print(f'This is your score: {self.player_human.player_score}')

        print("My cards:")
        self.player_comp.get_new_card(self.card_deck)
        self.player_comp.get_new_card(self.card_deck)
        print(self.player_comp.player_card)
        print(f'This is my score: {self.player_comp.player_score}')

    def _make_decision_for_comp_to_take_move(self):
        comp_score = self.player_comp.player_score
        human_score = self.player_human.player_score
        if human_score < comp_score <= 21:
            return False
        elif comp_score < human_score <= 21:
            return True
        elif human_score <= 21 < comp_score:
            return False
        elif comp_score <= 21 < human_score:
            return False
        else:
            return None

    def players_making_next_moves(self):
        self.player_human.make_next_moves(self.card_deck)
        if self._make_decision_for_comp_to_take_move():
            self.player_comp.make_next_moves(self.card_deck)
        print("It is look like you did all for me, I do not need any move....")

    def _how_is_the_winner(self) -> bool | None:
        comp_score = self.player_comp.player_score
        human_score = self.player_human.player_score
        print(f'The final result: My score is: {comp_score}'
              f' and your score is: {human_score}, so...')
        if human_score < comp_score <= 21:
            return False
        elif comp_score < human_score <= 21:
            return True
        elif human_score <= 21 < comp_score:
            return True
        elif comp_score <= 21 < human_score:
            return False
        elif comp_score == human_score:
            return None
        else:
            return None

    def how_is_the_winner_message(self):
        result = self._how_is_the_winner()
        if result:
            print(WINNER_MESSAGE_FOR_HUMAN)
        elif not result:
            print(WINNER_MESSAGE_FOR_COMP)
        elif result is None:
            print(MESSAGE_FOR_DRAW)
        else:
            print("Some strange/////")
