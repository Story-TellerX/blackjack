from card_v2 import CardDeckShuffle
from player_v2 import HumanPlayer, ComputerPlayer


class GameControl:

    def __init__(self):
        self.card_deck_class = CardDeckShuffle()
        self.player_human = HumanPlayer()
        self.player_comp = ComputerPlayer()
        self.card_deck = []

    def get_players_name(self) -> None:
        player_name_input = str(input("How can I call you protein man: "))
        self.player_human.player_name = player_name_input
        self.player_comp.player_name = "You can call me Blender"

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

    def get_next_human_moves(self) -> None:
        print("So take your moves")
        while True:
            if not self.player_human.check_player_score():
                print("SORRY THIS IS TOO MUCH")
                break
            if not self.player_human.ask_about_one_more_card():
                print(f"You are stopped and your score is: {self.player_human.player_score}")
                break
            self.player_human.get_new_card(self.card_deck)
            print(self.player_human.player_card)
            print(f'This is your new score: {self.player_human.player_score}')

    def get_next_comp_moves(self) -> None:
        print("So is is my turn")
        while True:
            if not self.player_comp.check_player_score():
                print("OH NO, THIS IS TOO MUCH!!!")
                break
            if not self.player_comp.ask_about_one_more_card():
                print("It is enough for me, I`m stop")
                print(f"and my score is: {self.player_comp.player_score}")
                break
            self.player_comp.get_new_card(self.card_deck)
            print(self.player_comp.player_card)
            print(f'This is my new score: {self.player_comp.player_score}')

    def _how_is_the_winner(self) -> bool | None:
        comp_score = self.player_comp.player_score
        human_score = self.player_human.player_score
        print(f'The final result: My score is: {comp_score}'
              f' and your score is: {human_score}, so...')
        # if comp_score > 21 and human_score > 21:
        #     print("no one winner here... Make one more round!")
        if human_score < comp_score <= 21:
            return False
        elif comp_score < human_score <= 21:
            return True
        else:
            return None

    def how_is_the_winner_message(self):
        result = self._how_is_the_winner()
        print(result)
        if result:
            print("Oh no it is impossible - YOU ARE WINNER")
        elif not result:
            print("I knew you would lose. The human brain cannot compete with mine.")
            print("I`m Blender most powerfully robot mind. I`M WINNER")
            print('I`m gonna build my own thing party with blackjack and hook...')
        elif result is None:
            print("no one winner here... Make one more round!")
        else:
            print("Some strange/////")
