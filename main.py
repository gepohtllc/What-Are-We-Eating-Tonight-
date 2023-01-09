import random

#INTRODUCTION - In it's current state, the user is allowed five entries for the randomizer to choose from. This is a project I plan on adding to as I learn more about Python. Enjoy!

print("What Are We Eating Tonight?")

#food_choices is a variable used to store the choices the user enters.
#this information is stored as a list and in theory can hold a large amount of entries.

food_choices = []

#currently, the users are only allotted 3 entries. Adding more than 3 can lead to the program crashing.
#using the append() function, each choice is appended to the food_choices list.

food_choices.append(input("\n Enter your first choice: "))
food_choices.append(input("\n Enter your second choice: "))
food_choices.append(input("\n Enter your third choice: "))
food_choices.append(input("\n Enter your fourth choice: "))
food_choices.append(input("\n Enter your last choice: "))

random_choice = random.choice(food_choices)

if random_choice == 0:
  print("\n You are eating " + str(random_choice) + " tonight!")
if random_choice == 1:
  print("\n You are eating " + str(random_choice) + " tonight!")
if random_choice == 2:
  print("\n You are eating " + str(random_choice) + " tonight!")
if random_choice == 3:
  print("\n You are eating " + str(random_choice) + " tonight!")
else:
  print("\n You are eating " + str(random_choice) + " tonight!")