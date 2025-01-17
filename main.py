from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
  if u_score==c_score:
      return "draw"
  elif c_score==0:
      return "computer won"
  elif u_score==0:
      return "you won"
  elif u_score>21:
      return "you lose"
  elif c_score>21:
      return "you won"
  elif u_score > c_score:
      return "you win"
  else:
      return "you lose "

def play():
    print(logo)
    user_cards=[]
    computer_cards=[]
    user_score=-1
    computer_score=-1
    game=True

    for i in range(2):
     user_cards.append(deal_card())
     computer_cards.append(deal_card())

    while game:
     user_score=calculate_score(user_cards)
     computer_score=calculate_score(computer_cards)
     print(f"Your cards: {user_cards}, current score: {user_score}")
     print(f"Computer's first card: {computer_cards[0]}")
     if user_score==0 or computer_score==0 or user_score>21:
        game=False
     else:
        deal=input("want to deal another card? ")
        if deal=='y':
            user_cards.append(deal_card())
        else:
            game=False
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("want to play?")=='y':
    play()


