import random, math, time
def chicken():
  multiplier = 1
  # i am trying to make the money system universal so i dont waste time - decided to make other stuff than gambling
  money = 200
  mulsum = 0
  chance = 0
  print("This is chicken Road! your goal is to make $2000 from this $200! \n ")
  notPlaying = True # i forgot why i added this, my main idea was to be able to break the loop but now i dont know why even break the loop, i now remember oh, i definetly remember now.
  while notPlaying:
    bet = int(input("Enter Bet: "))
    while bet > money:
      print("Not enough funds.")
      bet = int(input("Enter Bet: "))
    inMainLoop = True 
    while inMainLoop:
      notPlaying = False
      def choicenMoneySys():
        roundDone = False
        choice = input(f"Balance: ${money} \nThis is Chicken Road! Enter A to JUMP and B to COLLECT EARNINGS: ")
        def choiceSys():
          nonlocal money, choice, multiplier, mulsum, chance, inMainLoop, bet
          if (choice == "a") or (choice == "A"): #
            chance = chance = random.randint(1, 100)
            if chance <= 90:
              mulsum = multiplier * 1.17
              multiplier = mulsum
              print(f"You Win With {round(mulsum, 2)}x multiplier")
            else:
              print("CRASH!! Chicken Got Ran Over :'(")
              money -= bet
              roundDone = True
          if (choice == "b") or (choice == "B"):
            money += round(bet * (mulsum - 1))
            print(f"You Cashed Out With {round(mulsum, 2)}x and ${money}!")
            mulsum = 1
            roundDone = True
            if roundDone:
              bet = int(input("Enter Bet: "))
          
        choiceSys()
      choicenMoneySys()






# it really took time to think about how will i make russian roulette :broken_heart:
def russian_roulette():
  print("One of the nine bullet chambers has a bullet in it, DONT DIE.")
  rolls_player = 1
  while (rolls_player >= 9) or (rolls_player <= 0):
    rolls_player = int(input("You can only pick 1-8! ")) 
  
  bullet_pos = random.randint(1, 9)
  chance_of_bullet = 0.11
  chance_of_bullet = (chance_of_bullet * rolls_player)
  current_chamber = 0
  opponent_rolls = 0
  GFCR = ["You", "Opponent"] # it doesnt really matter what does this mean because i will use it once, but if you want to know it stands for going first chance rqndomizer
  goingFirst = GFCR[random.randint(0, 1)]
  bothAlive = True
  while bothAlive:
    if (goingFirst == "You"):
      rolls_player = int(input("\n \n \nhow many times you want to pull the lever? \n ")) 
      for i in range(rolls_player):
        time.sleep(1)
        current_chamber += 1
        chance_of_bullet += 0.11
        if (current_chamber != bullet_pos):
          print("CLICK! empty chamber")
        else:
          print("BOOM! You Died!")
          rolls_player = 0
          bothAlive = False
          break
      if bothAlive:
        goingFirst = "Opponent"
    if (goingFirst == "Opponent"):
      if (chance_of_bullet < 0.12):
        opponent_rolls = random.randint(1, 3)
        print(f"\n \n \nOpponent chooses to go {opponent_rolls} times \n ")
      elif (chance_of_bullet < 0.34):
        opponent_rolls = random.randint(1, 2)
        print(f"\n \n \nOpponent chooses to go {opponent_rolls} times \n ")
      else: 
        opponent_rolls = 1
        print(f"\n \n \nOpponent chooses to go {opponent_rolls} times \n ")
      for i in range(opponent_rolls):
        chance_of_bullet += 0.11
        time.sleep(1)
        current_chamber += 1
        if (current_chamber == bullet_pos):
          print("BOOM!! Opponent Loses")
          bothAlive = False
          break
        else:
          print("Click! empty chamber....")
      if bothAlive:
        goingFirst = "You"
      

  
  
  
  
russian_roulette()