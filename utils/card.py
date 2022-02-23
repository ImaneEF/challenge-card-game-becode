import random
from turtle import color

value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
icon = ["♠", "♥", "♦", "♣" ]

class Symbol():
    def __init__(self, icon):
        #self.color = color
        self.icon = icon
    

class Card(Symbol):
    def __init__(self, icon, value):
        super().__init__(icon)
        self.value = value
        

    def __str__(self):

        print("{} of {}". format(self.value, self.icon))











