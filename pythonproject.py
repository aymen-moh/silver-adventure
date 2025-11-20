import random, math
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
          if (choice == "a") or (choice == "A"):
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
  print("One of the nine bullet chambers has a bullet in it, DONT DIE.")
  
  
  
russian_roulette()