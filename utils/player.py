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

    def play(self):
        random_card = random.choice(self.cards)
        print(random_card)


class Deck():
    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for s in ["♥", "♦", "♣", "♠" ]:
            for v in range (len(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])):
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.__str__()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


deck = Deck()
deck.shuffle()
#deck.show()
card = deck.drawCard()
card.__str__()



