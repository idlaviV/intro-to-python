
## Conditions
# We have already talked about variables. We often need to compare and execute 
# code depending on certain conditions -> If-Statements

# we have the following logical conditions:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

age = 12
if age >= 18:
    print("Access granted!")
    
# indent is important!
    
# if we want to cover more than one case for one variable we can use 
# else statements, wich cover every poissible other case:
if age >= 18:
    print("Access granted!")
else:
    print("You are too young!")
    

# for even more cases we can use the elif statement:

number = 2
if number > 0:
    print("Positive value")
elif number == 0:
    print("Zero")
else:
    print("Negative vaulue")
    
# alternativly we could have used 2 elif statements, however its more common and
# good practice to have a fallback (else)


## Strings, Lists and Conditions
banned_players = ["Tim", "Jara", "Jackie", "Peter"]
name = "Tim"
if name in banned_players:
    print("You are banned!")

# we can negate using a not before a statement
if not name in banned_players:
    print("You are not banned!")
    
# the in keyword also works for strings:
if "hello" in "hello world":
    print("Contains!")
    
if not "hello" in "hello world":
    print("Contains no hello")
    
# we can check for multiple conditions in one if using and & or:
if age >= 18 and not name in banned_players:
    print("Acces granted")
else:
    print("Sorry :/")

## Truth table and:
# True and True = True
# True and False = False
# False and False = False
# False and True = False


## Truth table or:
# True or True = True
# True or False = True
# False or True = True
# False or False = False


## For Loops
# do someting x times
# start with 0, end with 10-1
for x in range(0, 10):
    print(x)

# range syntax:
# range(from, to, step)
for x in range(20, 30, 2):
    print(x)
    
# short version:
for x in range(10):
    print(x)
    
    
for x in range(0, len(banned_players)):
    print("index: ", x-1, banned_players[x])
    
# an easier way to go through a list:
for player in banned_players:
    print(player)
    
# the same works for strings (they are a list if characters)
# an easier way to go through a list:
for char in "Konstanz":
    print(char)
    
# last but no least, the enumerate function:
for index, player in enumerate(banned_players):
    print(index, player)


## While Loops
# do someting as long as a condition holds
# A basic loop:
x = 0 
while x < 3:
  print(x)
  x += 1


# Break statement
x = 1
while x < 6:
    print(x)
    if x == 3: 
        break # quit the loop
    
    
# Continue statement
skip_values = [3,5]
while x < 6:
    if x in skip_values: 
        continue # skip to the top of the loop
    print(x)    

    
    