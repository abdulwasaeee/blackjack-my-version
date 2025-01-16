logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

play=True

want=input("do you want to play? y/n ")
if want=='n':
    play=False

while play:
    print(logo)
    user_cards=[]
    dealer_cards=[]
    user_sum=0
    dealers_sum=0
    go_on=True
    dealer_cards.extend([random.choice(cards), random.choice(cards)])
    user_cards.extend([random.choice(cards), random.choice(cards)])
    user_sum = sum(user_cards)
    dealers_sum=sum(dealer_cards)
    if user_sum == 21 and dealers_sum == 21:
     print("draw")
     print(f"Your cards: {user_cards}, current score: {user_sum}")
     print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
    elif user_sum==21:
        print("you won")
        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
        go_on = False
    elif user_sum > 21:
        go_on = False
        print("you went over. you lose")
        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
    elif dealers_sum==21:
        print("you lost computer won")
        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
        go_on = False
    else:
        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {dealer_cards[0]}")
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == 'n':
          go_on = False
          while dealers_sum<17:
                     dealer_cards.append(random.choice(cards))
                     dealers_sum = sum(dealer_cards)
          if user_sum<21 and dealers_sum>21:
              print("you won")
              print(f"Your cards: {user_cards}, current score: {user_sum}")
              print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")

          if user_sum == 21 and dealers_sum == 21:
                 print("draw")
                 print(f"Your cards: {user_cards}, current score: {user_sum}")
                 print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
          if user_sum > 21:
                 print("you went over. you lose")
                 print(f"Your cards: {user_cards}, current score: {user_sum}")
                 print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
          if user_sum == 21:
                 print("you won")
                 print(f"Your cards: {user_cards}, current score: {user_sum}")
                 print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")

          if dealers_sum == 21:
                 print("you lost computer won")
                 print(f"Your cards: {user_cards}, current score: {user_sum}")
                 print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
          if user_sum<21 and dealers_sum<21:
              if user_sum<dealers_sum:
                 print("you lost computer won")
                 print(f"Your cards: {user_cards}, current score: {user_sum}")
                 print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")

              if dealers_sum<user_sum:
                 print("you won")
                 print(f"Your cards: {user_cards}, current score: {user_sum}")
                 print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")





    while go_on:
     dealer_cards.append(random.choice(cards))
     user_cards.append(random.choice(cards))
     user_sum=sum(user_cards)
     dealers_sum=sum(dealer_cards)
     if user_sum==21 and dealers_sum==21:
         print("draw")
         print(f"Your cards: {user_cards}, current score: {user_sum}")
         print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
     elif user_sum>21:
         print("you went over. you lose")
         print(f"Your cards: {user_cards}, current score: {user_sum}")
         print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
         go_on=False

     elif user_sum == 21:
         print("you won")
         print(f"Your cards: {user_cards}, current score: {user_sum}")
         print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
         go_on=False
     elif dealers_sum == 21:
         print("you lost computer won")
         print(f"Your cards: {user_cards}, current score: {user_sum}")
         print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
         go_on = False
     else:
         print(f"Your cards: {user_cards}, current score: {user_sum}")
         print(f"Computer's first card: {dealer_cards[0]}")
         hit=input("Type 'y' to get another card, type 'n' to pass: ")
         if hit=='n':
          go_on=False
          if dealers_sum < 16:
              while dealers_sum < 16:
                  dealer_cards.append(random.choice(cards))
                  dealers_sum = sum(dealer_cards)
          user_sum = sum(user_cards)
          if user_sum == 21 and dealers_sum == 21:
              print("draw")
              print(f"Your cards: {user_cards}, current score: {user_sum}")
              print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
          elif user_sum > 21:
              print("you went over. you lose")
              print(f"Your cards: {user_cards}, current score: {user_sum}")
              print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
          elif user_sum<21 and dealers_sum>21:
              print("you won")
              print(f"Your cards: {user_cards}, current score: {user_sum}")
              print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")


          elif user_sum == 21:
              print("you won")
              print(f"Your cards: {user_cards}, current score: {user_sum}")
              print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")

          elif dealers_sum == 21:
              print("you lost computer won")
              print(f"Your cards: {user_cards}, current score: {user_sum}")
              print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")
          elif user_sum < 21 and dealers_sum < 21:
              if user_sum < dealers_sum:
                  print("you lost computer won")
                  print(f"Your cards: {user_cards}, current score: {user_sum}")
                  print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")

              if dealers_sum < user_sum:
                  print("you won")
                  print(f"Your cards: {user_cards}, current score: {user_sum}")
                  print(f"computers cards: {dealer_cards}, current score: {dealers_sum}")

    play_again=input("want to play again? ")
    if play_again=='n':
     play=False
    if play_again == 'y':
        print("\n")
