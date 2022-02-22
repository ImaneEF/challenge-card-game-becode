value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
icon = ["♠", "♥", "♦", "♣" ]



#color dict of tuple maken

# loop to go through all of them: maybe in deck?
for i in range (0, len(self)):
            for j in range (0, len(suits)):
                card = (faces[i] + suits[j])