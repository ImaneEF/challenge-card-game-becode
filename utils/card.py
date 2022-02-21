# Make a symbol
import random
class Symbol():
    def __init__(self, color, icon):
        self.color = color
        self.icon = ("♠", "♥", "♦", "♣")
    

class Card(Symbol):
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value