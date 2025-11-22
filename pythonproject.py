import random, math, time, threading
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
def russian_roulette():
  def oneP():
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
  def twoP(): 
    P1N = input("Enter Player 1 name")              
    P2N = input("Enter Player 2 name")              #
    sPlaying = True            
    bullet = random.randint(1, 9)
    cChamber = 0 
    pList = (1, 2) 
    cPlaying = pList[random.randint(0, 1)] 
    acceptable_choices = (1, 2, 3, 4, 5, 6, 7, 8)
    print(cPlaying)
    while sPlaying:
      while (cPlaying == 1):
        P1C = int(input(f"How many times would ({P1N}) like to fire?"))
        while P1C not in acceptable_choices:
          P1C = int(input("Please Enter Numbers 1-8! "))
        
        for i in range(P1C):
          time.sleep(0.65)
          cChamber += 1
          if cChamber == bullet:
            print(f"{P1N} died ;(")
            sPlaying = False
            break
          else:
            print("CLICK! Empty Chamber")
        cPlaying = 2
      while (cPlaying == 2):
        P2C = int(input(f"How many times would ({P2N}) like to fire?"))
        while P2C not in acceptable_choices:
          P2C = int(input("Please Enter Numbers 1-8! "))
        
        for i in range(P2C):
          time.sleep(0.65)
          cChamber += 1
          if (cChamber == bullet):
            print(f"{P2N} died! ;(")
            sPlaying = False
            break
          else:
            print("CLICK! Empty Chamber")
        cPlaying = 1
  c = int(input("Number of Players: "))
  while True:
    if c == 1:
      oneP()
    elif c == 2:
      twoP()
    else:
      c = int(input("Please choose ohe or two players"))
def hilo(): # this include no code from gess.py!
  randomNum = random.randint(1, 13)
  choices = ["h", "l", "H", "L", "Higher", "Lower", "HIGHER", "LOWER", "higher", "lower"] #
  while True:
    UD = [0, 1]
      
    
    choice = input(f"{randomNum} Higher Or Lower? ")
    last = randomNum
    while True:
      if (choice == "higher") or (choice == "Higher") or (choice == "HIGHER") or (choice == "h") or (choice == "H"):
        randomNum = random.randint(1, 13)
        if (randomNum == last):
          PUD = UD[random.randint(0, 1)]
          if (PUD == 0):
            randomNum -= 1
          if (PUD == 1):
            randomNum += 1
        elif (randomNum < last):
          print(f"You Lost! it was {randomNum}")
          break
        else:
          print(f"You Won! it was {randomNum}")
          break
      elif (choice == "lower") or (choice == "Lower") or (choice == "LOWER") or (choice == "l") or (choice == "L"):
        randomNum = random.randint(1, 13)
        if (randomNum == last) and not (randomNum == 13) and not (randomNum == 1):
          PUD = UD[random.randint(0, 1)]
          if (PUD == 0):
            randomNum -= 1
          if (PUD == 1):
            randomNum += 1
        elif (randomNum > last):
          print(f"You Lost! it was {randomNum}")
          break
        else:
          print(f"You Won! it was {randomNum}")
          break
      while choice not in choices:
        choice = input("Please Enter a Valid Choice: higher, lower, Higher, Lower, HIGHER, LOWER, H, L, h, l ")
def paperRedstone():
  Redstone = False
  Paper = False
  while True:
    choice = input("Choose Paper (P) or Redstone (R) or Help (H)")
    if (choice == "P") or (choice == "p"):
      Paper = True
      break
    elif (choice == "R") or (choice == "r"):
      Redstone = True
      break
    elif (choice == "h") or (choice == "H"):
      print("Paper game is a minecraft inspered game where there are 2 droppers \n with paper and redstone named numbers that are 1 to 9, \n a lever is placed to fire both droppers and the higher number wins, this \n game was inspired by it") # Sorry for poor quality explanation its almost 5 am
    else:
      print("Please Enter P, R or H")
  def dispense():
    DP = random.randint(1, 9)  # Paper dispenser 
    DR = random.randint(1, 9)   # Redstone dispenser
    if Paper:
      if DP > DR:
        print("You Won!")
      else:
        print("You Lost!")
    if Redstone:
      if DP < DR:
        print(f"Redstone: {DR}, Paper: {DP}, You Won!")
      else:
        print(f"Redstone: {DR}, Paper: {DP}, You Lost!")
  
  
  
  dispense()
def armorGame():
  
  
  hel = ("Helmet", "helmet", "HELMET", "H", "h")
  chestplate = ("Chestplate", "chestplate", "c", "C", "CHESTPLATE")
  leggings = ("leggings", "Leggings", "LEGGINGS", "L", "l")
  boots = ("Boots", "boots", "BOOTS", "b", "B")
  armor = ("helmet", "chestplate", "leggings", "boots")
  
  
  shuffle = armor[random.randint(0, 3)]
  
  
  
  
  
  
  money = 50000
  current_bal = money
  print(f"This is armorGame, your goal is to make a million dollars, You have ${current_bal}")
  bet = int(input("Enter Bet: "))
  while (bet > money):
    print(f"You only have ${money}!")
    bet = int(input("Enter bet again: "))
  r = True
  while r:
      choice = input("Choose armor peice: ")
      if (shuffle == choice):
        money -= bet
        money += bet * 4
        print(f"YOU WIN!! 4x You have {money}")

def dialog():
  
  i = input("Welcome to PythonPr! \n \nplease enter one of the following commands! \n \n/chicken - chicken road game! \n/russian - russian roulette game (9 barrels \n/hilo - 1-13, guess if the next number will be higher or lower! \n/paperRedstone - minecraft inspired game! \n/armorGame - another minecraft game where a dispenser sits near and 1 out of 4 times you will win! (4x)")
  while True:
    if (i == "/chicken"):
      chicken()
    if (i == "/russian"):
      russian_roulette()
    if (i == "/hilo"):
      hilo()
    if (i == "/paperRedstone") or (i == "/paperredstone"):
      paperRedstone()
    if (i == "/armorGame"):
      armorGame()
    
    
    
dialog()