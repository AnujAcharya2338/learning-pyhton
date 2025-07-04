# import random

# random_integer=  random.randint(1,2)
# print(random_integer)
# random_float=  random.random()
# print(random_float)

# love_score=random.randint(0,100)
# print(f"Your love score is {love_score}")

# fruits = ["cherry", "apple", "banana"]
# print(fruits[-1])
# fruits[-1] = "Orange"
# print(fruits[-1])
# fruits.append("Boboya")
# print(fruits)

import random
scissors= '''    
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)

'''

rock='''
           _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)     '''


paper='''          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)'''


game_images= [rock, paper, scissors]
ans=int(input("What do  you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if ans >= 3 or ans < 0:
 print("Invalid number ")
else:
  print(game_images[ans])
  comp=int(random.randint(0,2))
  
  print("Computer choose:")
  print(game_images[comp])
  if ans == 0 and comp == 2:
    print("You Win!")
  elif ans >= 3 or ans < 0:
   print("Invalid number ")
  elif comp > ans:
    print("You lose!") 
  elif comp==ans: 
    print("Its a draw!")
  elif comp == 0 and ans == 2:
   print("You lose!")
  elif ans > comp:
   print("You win!")
  
  
 
















