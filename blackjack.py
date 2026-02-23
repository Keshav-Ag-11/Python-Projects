import random
from logo import logo
print(logo)
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
comp = []
human=[]
for i in range (2):
    comp.append(deal_card())
    human.append(deal_card())
c= sum(comp)
h= sum(human)
print(f"Your cards: {human}, current score: {h}")
print(f"Computer's first card: {comp[0]}")
while True:
    choice = input("Type 'y' to get another card , type 'n' to pass")
    if choice == 'n':
        while c<17:
            card = deal_card()
            comp.append(card)
            c= sum(comp)
        if c>21:
            print("You win!")
            print("Computer cards:", comp)
            print("Computer score:", c)
        elif c<21 and c>h:
            print("Computer wins!")
            print("Computer cards:", comp)
            print("Computer score:", c)
        elif c<21 and c<h:
            print("You win")
            print("Computer cards:", comp)
            print("Computer score:", c)
        elif c == h:
            print("Draw")
            print("Computer cards:", comp)
            print("Computer score:", c)
        break
    elif choice == 'y':
        card=deal_card()
        human.append(card)
        h=sum(human)
        print(f"Your cards: {human}, current score: {h}")
        if h>21:
            print("Computer wins!")
            print("Computer cards:", comp)
            print("Computer score:", c)
            break





