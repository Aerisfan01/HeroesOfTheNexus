import random

#Attempting to use Class for the substats
class Card:
    def __init__(self, name, cost, attack, health, card_type):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.card_type = card_type
    def __str__(self):
        return f"{self.name} (Cost: {self.cost}, ATK: {self.attack}, HP: {self.health}, DEF: {self.defense}, Type: {self.card_type})"
        
    def attack_card(self, other_card): #Attack Formula
        other_card.health -= self.attack
        self.health -= other_card.attack
        
        if self.health <= 0:
            self.is_alive = False
            
        if other_card.health <= 0:
            other_card.is_alive = False
            
        self.is_attacking = False
        
    def defend(self, other_card): #Defense of cards 
        self.defense += other_card.attack
        
        if self.defense > 0:
            self.is_attacking = False


#Define deck for the card draw usage for the players 
class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw_card(self):
        return self.cards.pop(0)
        
    def add_card(self, card):
        self.cards.append(card) 

class DemonGod(Card): #aatrox card 
    def __init__ (self):
        super().__init__("Demon God", 4, 5, 10, 3, "Tank") #Name, DP cost, Attack, HP, Defense and Subclass

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.board = []
        self.max_mana = 0
        self.current_mana = 0
        
    def draw_card(self):
        card = self.deck.draw_card()
        self.hand.append(card)
        
    def play_card(self, card_index):
        card = self.hand.pop(card_index)
        
        if self.current_mana < card.cost:
            print("You don't have enough mana to play that card.")
            self.hand.append(card)
        else:
            self.current_mana -= card.cost
            self.board.append(card)
            print(f"{self.name} played {card.name}.")
        
                          
