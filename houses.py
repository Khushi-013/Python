# The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

# 🦁 Gryffindor
# 🦅 Ravenclaw
# 🦡 Hufflepuff
# 🐍 Slytherin


# Write a program that asks the user some questions with the int() and input() functions:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

# If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
# Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
# Else, output the message "Wrong input."
# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

# If the answer is 1, Hufflepuff +2.
# Else if answer is 2, Slytherin +2.
# Else if answer is 3, Ravenclaw +2.
# Else if answer is 4, Gryffindor +2.
# Else, output the message "Wrong input."
# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

# If the answer is 1, Slytherin +4.
# Else if the answer is 2, Hufflepuff +4.
# Else if the answer is 3, Ravenclaw +4.
# Else if the answer is 4, Gryffindor +4.
# Else, output "Wrong input."
# Lastly, print out the house with the most points!


# Write code below 💖

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
answer = int(input("Enter 1 or 2: "))

if answer ==1:
  gryffindor +=1
  ravenclaw +=1
elif answer ==2:
  hufflepuff +=1
  slytherin +=1
else:
  print("Wrong input.")


print("Q2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer = int(input("Enter 1,2,3 or 4: "))

if answer == 1:
  hufflepuff +=2
elif answer == 2:
  slytherin +=2
elif answer == 3:
  ravenclaw +=2
elif answer == 4:
  gryffindor +=2
else:
  print("Wrong input.")


print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer = int(input("Enter 1,2,3 or 4: "))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print("Wrong input.")


houses = {"Gryffindor": gryffindor, "Ravenclaw": ravenclaw, "Hufflepuff": hufflepuff, "Slytherin": slytherin}
sorted_houses = sorted(houses.items(), key=lambda x: x[1], reverse=True)
house = sorted_houses[0][0]

print(f"\nThe Sorting Hat has sorted you into... {house}!")
