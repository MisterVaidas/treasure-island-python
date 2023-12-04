# Final project: Treasure Island 1.0

print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************    
''')

print("Welcome to Treasure Island, a land of mystery and adventure.")
print("Your mission is to find the hidden treasure. Choose wisely and good luck!")

first_task = input("You're at a crossroad in a dense forest. Will you go 'left' towards the whispering hills or 'right' into the dark woods? \n")

if first_task == "left":
  second_task = input("You come upon a serene lake with a mysterious island in the middle. Will you 'wait' for a boat or 'swim' across the shimmering waters? \n")
  if second_task == "wait":
    third_task = input("You arrive at the island and find an ancient house with three mystical doors: one red, one yellow, and one blue. Which door do you choose? \n")
    if third_task == "blue":
      print("Congratulations! Behind the blue door, you find a room filled with glittering treasure! You've won the game!")
    elif third_task == "red":
      print("You open the red door and are met with a blinding light. You've triggered an alarm and are captured! Game over.")
    elif third_task == "yellow":
      print("Behind the yellow door, you find a room that suddenly locks behind you. Trapped forever. Game over.")
    else:
      print("You hesitate and choose none of the doors. The island vanishes, and you're left stranded. Game over.")
  else:
    print("As you swim across the lake, a whirlpool drags you under. Game over.")
else:
  print("You venture right into the woods and eventually lose your way. Game over.")