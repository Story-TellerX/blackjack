from card_v2 import CardDeckShuffle
from const import WINNER_MESSAGE_FOR_COMP, GREETING_PLAYER_TEXT, COMP_NAME_INTRODUCTION
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

    def player_make_next_move(self):
        list_of_players = [self.player_human, self.player_comp]
        for player in list_of_players:
            if player is self.player_human:
                print("Make your move...")
            else:
                print("My turn")
            self._make_player_move(player)

    def _make_player_move(self, player):
        while True:
            if not player.check_player_score():
                print("SORRY THIS IS TOO MUCH")
                break
            if not player.ask_about_one_more_card():
                print(f"So, score is: {player.player_score}")
                break
            player.get_new_card(self.card_deck)
            print(player.player_card)
            print(f'This is new score: {player.player_score}')

    def _how_is_the_winner(self) -> bool | None:
        comp_score = self.player_comp.player_score
        human_score = self.player_human.player_score
        print(f'The final result: My score is: {comp_score}'
              f' and your score is: {human_score}, so...')
        if human_score < comp_score <= 21:
            return False
        elif comp_score < human_score <= 21:
            return True
        else:
            return None

    def how_is_the_winner_message(self):
        result = self._how_is_the_winner()
        if result:
            print("Oh no it is impossible - YOU ARE WINNER")
        elif not result:
            print(WINNER_MESSAGE_FOR_COMP)
        elif result is None:
            print("no one winner here... Make one more round!")
        else:
            print("Some strange/////")
