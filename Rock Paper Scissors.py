rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

gameImages = [rock, paper, scissors]
print("Welcome to Rack Paper Scissors Game!")

chooseOfComp = random.randint(0,2)
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

if(0<=choose<=2):
    print("You chose:\n" + gameImages[choose])
    print("Computer chose:\n" + gameImages[chooseOfComp])

if choose - chooseOfComp == 1 or choose - chooseOfComp == -2:
    print("You win.")
elif choose - chooseOfComp == -1 or choose - chooseOfComp == 2:
    print("You lose.")
elif choose == chooseOfComp:
    print("You drew.")
else:
    print("You Typed an Invalid Number!")
