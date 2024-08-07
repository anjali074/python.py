import random

suits = ["clubs", "spades", "diamonds", "hearts"]
face = ["jack", "queen", "king", "ace"]
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create the deck of cards
deck = set((card, "of", suit) 
    for suit in suits 
      for card in face + numbered)

def draw():
    card = random.choice(list(deck))
    deck.remove(card)
    return card

# Draw 20 cards
for _ in range(20):
    print(draw())

print(len(deck))