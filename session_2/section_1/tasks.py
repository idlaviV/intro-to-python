# ------------------------------------------------------------------------------#
# (1) 
# guess the number game
# We are using the random lib to generate a random number between 0 and 100
# and store it in the variable r.
# Write a program which prompts the user until the input is equal to the random
# number.

import random

r = random.randint(0, 100)
prompt = int(input("Please guess 0 <= r < 100 (type -1 for hint): \n>"))
while prompt != r:
    if prompt < r:
        print("Too low")
    else:
        print("Too high")
    if prompt < 0:
        print(f"Hint: {r}")
    prompt = int(input(f"Guess again! \n>"))
print("You got it!")

##############
##############
r = random.randint(0, 100)
while True:
    prompt = int(input(f"Please guess 0 <= r < 100 (type -1 for hint): \n>"))
    if prompt < r:
        print("Too low")
    elif prompt > r:
        print("Too high")
    else:
        print("You got it!")
        break
    if prompt < 0:
        print(f"Hint: {r}")

# Modify your program with hints concerning the guessed number (greater, lower)


# ------------------------------------------------------------------------------#
# (2)
# this is a short version to create a list from 0 to 19
numbers = list(range(20))

# print out only even numbers
for i in numbers:
    if i % 2 == 0:
        print(i)
