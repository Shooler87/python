import random
import sys
from random import shuffle
from time import sleep


class WarCards:
    deck = []

    cards = [
        ["2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "W♠", "D♠", "K♠", "A♠"],
        ["2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "W♣", "D♣", "K♣", "A♣"],
        ["2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "W♥", "D♥", "K♥", "A♥"],
        ["2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "W♦", "D♦", "K♦", "A♦"]
    ]

    with_jokers = False
    with_visible_simulation = False
    interval = 0
    time_per_single_draw = 3
    time_per_war = 12
    tiredness_factor = 1.00 # todo add tiredness for slower draws every x seconds or draws
    player1 = []
    player2 = []
    player1table = []
    player2table = []
    player1_draws_won = 0
    player2_draws_won = 0
    fight_counter = 0
    draw_counter = 0

    def __init__(self, with_jokers: bool = False, with_visible_simulation: bool = False, interval: float = 0.01):
        self.with_jokers = with_jokers
        self.with_visible_simulation = with_visible_simulation
        self.interval = interval
        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        for suit in self.cards:
            for card in suit:
                self.deck.append(card)

        if self.with_jokers:
            for suit_symbol in "♠♣♥♦":
                self.deck.append("J" + suit_symbol)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def split_cards(self):
        i = 0
        for card in self.deck:
            self.player1.append(card) if i % 2 == 0 else self.player2.append(card)
            i += 1

    def draw_cards(self):
        print("DRAW CARDS")
        while True:
            if self.with_visible_simulation:
                print(f"{"DRAW CARDS":-<40s}")
                sleep(self.interval)
            try:
                self.player1table.append(self.player1.pop(0))
                self.player2table.append(self.player2.pop(0))
                self.draw_counter += 1
                self.show_players_tables()
                self.check_tables()
            except IndexError:
                self.show_error("One of the hands is empty")
                self.show_stats()
                return
            except RecursionError:
                self.show_error("OH NO, THE WORST")
                self.show_stats()
                return

    def check_tables(self):
        len1table = len(self.player1table)
        len2table = len(self.player2table)
        # only one card per player
        if len1table == len2table == 1:
            if self.get_card_value(self.player1table[0]) > self.get_card_value(self.player2table[0]):
                self.take_cards("p1")
            elif self.get_card_value(self.player1table[0]) < self.get_card_value(self.player2table[0]):
                self.take_cards("p2")
            else:
                print("FIGHT!")
                self.fight()
                self.check_tables()  # recursion
        # typical situation for a fight
        elif len1table == len2table and (len1table % 3 == 0 or len1table % 2 == 1):
            if self.get_card_value(self.player1table[-1]) > self.get_card_value(self.player2table[-1]):
                self.take_cards("p1")
            elif self.get_card_value(self.player1table[-1]) < self.get_card_value(self.player2table[-1]):
                self.take_cards("p2")
            else:
                print("FIGHT CONTINUES!")
                self.fight()
                self.check_tables()  # recursion
        else:
            self.show_error("AAAAAAAAAAAAAA")

    def fight(self):
        if len(self.player1table) == len(self.player2table) == 1:
            self.fight_counter += 1
        # todo optional draw from other player when cannot continue the fight
        try:
            self.player1table.append(self.player1.pop(0))
            self.player1table.append(self.player1.pop(0))
            self.player2table.append(self.player2.pop(0))
            self.player2table.append(self.player2.pop(0))
        except IndexError:
            self.show_error("One of the hands is empty, cannot continue the fight")
            self.show_stats()
            exit()
        self.show_players_tables()

    @staticmethod
    def get_card_value(card: str) -> int:
        card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "W", "D", "K", "A", "J"]
        return card_order.index(card[:-1])

    def take_cards(self, player: str):
        tables = self.player1table + self.player2table
        shuffle(tables)
        if player == "p1":
            if self.with_visible_simulation:
                print(f"{"Player 1 wins this draw"}")
            self.player1 += tables
            self.player1_draws_won += 1
        elif player == "p2":
            if self.with_visible_simulation:
                print(f"{"Player 2 wins this draw"}")
            self.player2 += tables
            self.player2_draws_won += 1
        else:
            self.show_error("Cannot take cards")
            self.show_players_tables()

        self.player1table = []
        self.player2table = []

    def check_winner(self):
        if len(self.player1) == 0:
            print("Player 2 WON!")
        elif len(self.player2) == 0:
            print("Player 1 WON!")
        else:
            self.show_error("NO WINNERS THIS TIME")

    def show_draw_counter(self):
        print("draw counter:", self.draw_counter)

    def show_estimated_game_time(self):
        time_total = (self.draw_counter * self.time_per_single_draw + self.fight_counter * self.time_per_war) // 60

        if time_total > 60:
            temp = time_total // 60
            time_total = str(temp) + (" hour " if temp == 1 else " hours ") + str(time_total - temp * 60) + " minutes"
        else:
            time_total = str(time_total) + " minutes"

        print("estimated game time:", time_total)

    def show_estimated_watch_time(self):
        time_total = (self.draw_counter + self.fight_counter) // 60
        if time_total > 60:
            temp = time_total // 60
            time_total = str(temp) + (" hour " if temp == 1 else " hours ") + str(time_total - temp * 60) + " minutes"
        else:
            time_total = str(time_total) + " minutes"
        print(f"It would take {time_total} if you have watched every draw for one second")

    def show_fight_counter(self):
        print("fight counter:", self.fight_counter)

    def show_players_tables(self):
        print("Player 1 table:", self.player1table)
        print("Player 2 table:", self.player2table)

    def show_player_draw_counter(self):
        print(f"Player 1 took {self.player1_draws_won} draws")
        print(f"Player 2 took {self.player2_draws_won} draws")

    def show_deck(self):
        print("Shuffled deck:", self.deck)

    def show_player_cards(self):
        print("Player 1 cards:", self.player1)
        print("Player 2 cards:", self.player2)

    def show_stats(self):
        print(f"{"STATS":-^40s}")
        self.show_player_cards()
        self.show_players_tables()
        self.show_draw_counter()
        self.show_fight_counter()
        self.show_player_draw_counter()
        self.check_winner()
        self.show_estimated_game_time()
        if self.interval != 1.0:
            self.show_estimated_watch_time()

    @staticmethod
    def show_error(s: str):
        print(s, file=sys.stderr)


wc = WarCards(with_jokers=True, with_visible_simulation=True, interval=0.001)
wc.show_deck()
wc.split_cards()
wc.show_player_cards()
wc.draw_cards()
