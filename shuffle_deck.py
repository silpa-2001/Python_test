import random
shapes=["Spades","Clubs","Diamonds","Hearts"]
cards=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

deck=[f'{card} of {shape}' for shape in shapes for card in cards]

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

shuffle_cards= shuffle_deck(deck)

for x in shuffle_cards:
    print(x)