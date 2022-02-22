import sys
sys.path.append(r'C:\Users\epcs\OneDrive\Documenten\GitHub\challenge-card-game-becode\utils')
from card import Card
import random
from typing import List

class Player():
    def __init__(self, cards: List[Card], turn_count: int, number_of_cards: int, history):
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = history

    def play():
        random_card = random.choice(self.cards)
        print(random_card)


class Deck():
    def __init__(self, cards: List[Card]):
        for i in range (0, len(self)):
            for j in range (0, len(suits)):
                card = (faces[i] + suits[j])
                deck.append(card)
        print(deck)




