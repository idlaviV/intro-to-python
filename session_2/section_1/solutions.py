#------------------------------------------------------------------------------#
# (1) 
# guess the number game
# We are using the random lib to generate a random number between 0 and 100
# and store it in the variable r.
# Write a programm which prompts the user until the input is equal to the random
# number.

import random
r = random.randint(0,100)

# Modify your programm with hints concerning the guessed number (greater, lower)

MAX_GUESS_COUNT = 5
guess_count = 0
while True:
  if guess_count >= MAX_GUESS_COUNT:
    print(f"Too many guesses ({guess_count}). The random number is: {r}")
    break
  guess = int(input("Guess the number: "))  
  if guess == r:
    print("Correct!")
    break
  elif r > guess:
    print("Guess higher.")
  else:
    print("Guess lower.")
  guess_count += 1 

#------------------------------------------------------------------------------#
# (2)
# this is a short version to create a list from 0 to 19
numbers = list(range(20)) 

# print out only even numbers

for num in numbers:
    if num % 2 == 0:
        print(num)