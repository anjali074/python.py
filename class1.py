import random
suit=["clubs","Speder","Diamond","Heart"]
face=["jack","Queen","King","Ace"]
number=[2,3,4,5,6,7,8,9,10]

def draw():
  the_suit=random.choice(suit)
  the_card=random.choice(face + number)
  return(the_card,"of",the_suit)
for _ in range (20):
  print(draw())

deck=set()
suits=["clubs","Speder","Diamond","Heart"]
faces=["jack","Queen","King","Ace"]
number=[2,3,4,5,6,7,8,9,10]
for suit in suits:
  for card in face+number:
    deck.add((suit,card))
  print(deck)
card = random.choice(list(deck))
print("\n Card")
print(card)
deck_list = list(deck)
print("\nType of deck_list")
print(type(deck_list))
