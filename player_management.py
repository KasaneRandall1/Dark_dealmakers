import json,random
import os

class player():
    def __init__(self) -> None:
        self.health = 100
        self.deck = []
        self.deck_backup = []
        self.discard = []
        self.hand = []
        self.cards_drawn = False
        self.set_cards = False
        self.choose_target = False
        self.switch_turn = False
        self.monster_defeated = 0

    def __draw_start_deck(self):
        if os.path.isfile("data/player_cards.json"):
            with open("data/player_cards.json","r") as loaded_cards:
                cards = json.load(loaded_cards)
                self.deck = random.sample(cards,20)
                self.deck_backup = self.deck.copy()

    def __shuffle_deck(self):
        random.shuffle(self.deck)

    def __discard_hand(self):
        for i in self.hand:
            self.discard.append(i)
        self.hand.clear()

    def __shuffle_discard_back(self):
        draw_cards = len(self.deck)
        for i in range(draw_cards):
            self.hand.append(self.deck[i])
        for i in self.discard:
            self.deck.append(i)
        random.shuffle(self.deck)
        missing_card = 5 - draw_cards
        for i in range(missing_card):
            self.hand.append(self.deck[i])

    def deck_creation(self):
        self.__draw_start_deck()
        self.__shuffle_deck()

    def draw_hand(self):
        if len(self.deck) < 4:
            self.__shuffle_discard_back()
        for i in range(0,4):
            self.hand.append(self.deck[i])
        for i in self.hand:
            x = self.deck.index(i)
            self.deck.pop(x)

    def change_health(self,amount:int):
        self.health += amount
        if self.health < 0:
            self.health = 0

    def end_turn(self):
        self.__discard_hand()
        
    def reset(self):
        self.health = 100
        self.deck = []
        self.discard = []
        self.hand = []
        self.cards_drawn = False
        self.set_cards = False
        self.choose_target = False
        self.switch_turn = False