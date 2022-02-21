# Make a symbol
import random
class Symbol():
    def __init__(self, color, icon):
        self.color = color
        self.icon = ("♠", "♥", "♦", "♣")
    

class Card(Symbol):
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = ('A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')