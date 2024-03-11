import random,os,json

class cpu():
    def __init__(self) -> None:
        self.health = 5
        self.deck = []
        self.hand = []
        self.discard = []
        self.attacks = []
    def deck_create(self):
        self.__draw_start_deck()
        self.__shuffle_deck()
    def __draw_start_deck(self):
        if os.path.isfile("data/cpu_cards.json"):
            with open("data/cpu_cards.json","r") as loaded_cards:
                cards = json.load(loaded_cards)
                self.deck = random.sample(cards,20)
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
        missing_card = 4 - draw_cards
        for i in range(missing_card):
            self.hand.append(self.deck[i])
    def __draw_hand(self):
        if len(self.deck) < 4:
            self.__shuffle_discard_back()
        for i in range(0,4):
            self.hand.append(self.deck[i])
        for i in range(0,4):
            self.deck.pop(0)
    def end_turn(self):
        self.__discard_hand()
        return 1
    
    def reset(self):
        self.health = 30
        self.deck = []
        self.hand = []
        self.discard = []
    
    def __set_attacks(self,p_field,field):
        if len(p_field) <= len(field):
            for i in range(len(p_field)):
                self.attacks.append((i,i))
        else:
            for i in range(len(field)):
                self.attacks.append((i,i))

    def play_cards(self,field:list,player_field:list):
        set_cards = True
        self.__draw_hand()
        while set_cards:
            if len(field) < 5 and len(self.hand) !=0 and self.health > 3:
                field.append(self.hand[0])
                self.hand.pop(0)
                self.health -= 3
            else:
                set_cards = False
        self.__set_attacks(player_field,field)
        return field
                    


    