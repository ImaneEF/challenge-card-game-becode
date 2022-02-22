import sys
sys.path.append(r'C:\Users\epcs\OneDrive\Documenten\GitHub\challenge-card-game-becode\utils')
from card import Card
import random
from typing import List
class Player():
    def __init__(self, cards: List[Card], turn_count: int, number_of_cards: int, history):
        self.cards = [4]
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = history

    def play():
        random_card = random.choice(Card)
        print(random_card)



