# print("What is your height in cm?")
# height=int(input("Enter your height"))
# bill=0 
# if height > 120:
#   print("You are eligiable")
#   age=int(input("Enter Your Age"))
#   if age < 12:
#     bill=5
#     print("Child tickets are $5")
#   elif age<= 18:
#     bill=7
#     print("Youth tickets are $7")
#   elif age >=45 and age<=55:
#     print("Your ticket is free boomer")
#   else:
#     bill=12
#     print("Adtly tickets are $12")

#   photo=input("Do you want a photo taken? Y or N. ")
#   if photo=="Y":
#     bill += 3
#     print(f"Your final bill is {bill}")
# else:
#  print("You are not eligiable")


print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')

print("Welcome to treasure Island")
print("Your mission is to find the treasure")
choice1=input('You\'re at cross road. Where do you want to go? Type "left" or "right" ').lower()
if choice1 == "left":
 choice2=input('You\'ve come to a lake. Do you want to wait for a boat or swim? Type "boat" or "swim"').lower()
 if choice2 == "boat":
   choice3=input('You\'ve arrived at the house near a island unharmed. Choose a door in which the treasure is behind. Choose between "Red" or "Blue" or "Yellow"').lower()
   if choice3 == "red":
      print("Local canibals from island came and have a thanksgiving")
   elif choice3 == "blue":
      print("A mermaid emerges from water and rotates its monofin to send you back to your starting point.")
   elif choice3 == "yellow":
      print('Congragulations, You have aquired the great treasure. The treasure was "The friends you have made along the journey" and "Not getting chokeslamed by Mother Teressa"')
   else:
      print("You died of Organ failure. Choose different color")
 else:
    print("You got jumped by bunch of flying elephants. The force of their ears flapping caused a massive whirlpool which opened a portal for multiverse from which Mother Teresa came and beat the shit out of you.")
else:
  print("you are immortal and you got launced into space and you are heading towards a big blace hole with a massive gravitational pull where you will spend your eternity travelling through the unknowing void")

  
