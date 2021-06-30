
# Printing, Calculator, Variables & Types

## Basics printing
print("Hello World!")

# strings can be seperated/added via the plus sign
print("My name is " + "Tilman!")

## Escaping quotes
# A String is a sequence of characters, identified/between quotes: '', ""
# A second quotes to a first one marks the end of the string
# If we want to use quotes in our string we have to escape them or 
# use other quotes as string delimiters

print('My name is O\'Brian!')

print("My name is O'Brian!")

print("\"Wow!\", he said.")

print('"Wow!", he said.')


## Basic calculator
# we can perform any basic operation via the respective symbols
# this works
2+2
1-1
100*13
123/98
# modulo is supported as well
30%2

# the above works, however does not print/return anything
# in order to display the result, we have to print it

print(2+2)
print(123/98)
print(30%2)


# python recognices BODML
print(2+4*2)
print((2+4)*2)

# potenzen
print(2**3)
print(5**2)

## Variables
# If we want to store the result of our calculation or simply our name we can 
# assign a value to a variable

name = "Tilman"
age = 22
height = 1.78

# suppose I grew every year of my life the same amount:
# meaningfull names (yt py)
# good practice / standard in python is 'snake case':
growth_per_year = height * 100 / age

print(growth_per_year)

# if we want to print our growth per year combined with a string, like this:
# My growth per year is: 8.1, we might think the following will work:
# > print("My growth per year is: " + growth_per_year) 
# However, this will throw an error:
# > TypeError: can only concatenate str (not "int") to str

## Types
# There are different types in Python. The ones we focus on now are: 
# integers or int
persons = 10
number_of_apples = 1203

# if we want to update a value we can do this in two ways:
persons = persons + 1
persons += 1

# this works for all operations:
persons *= 2
persons /= 10
persons **= 2
persons -= 1000

# floats or float
height = 2.02
growth_per_year

# for floats we might want to round them - this ca be done via the round method:
# syntax: round(number, round_position)
# round_position: 0 round 1er, -1 round 10er, -2 round 100er, 
# 1 round 0.x, 2 round 0.0x
round(height, 1)

val = 126.471
round(val, 0)
round(val, -1)
round(val, -2)
round(val, 1)
round(val, 2)

# strings or str
name = "Leonhard Euler"
four = "4"
four_word = "four"
job = 'Mathematician'
bio = """was a Swiss mathematician, physicist, astronomer, geographer, 
logician and engineer who who made important and influential discoveries in 
many branches of mathematics, such as infinitesimal calculus and graph theory, 
while also making pioneering contributions to several branches such as topology 
and analytic number theory.
"""
source_url = "https://en.wikipedia.org/wiki/Leonhard_Euler"


# we can convert variables:

float_age = float(age)
int_height = int(height)
four_int = int(four)
# int + float
# four_word_int = int(four_word) # error
str_growth_per_year = str(growth_per_year)

# so now we can print our growth:
print("My growth per year is: " + str_growth_per_year) 

# If we don't want to handle conversions of types for printing we can use 
# formatted strings: f"... {variable} {another_variable}":
print(f"My name is {name}")
print(f"My growth per year is: {growth_per_year}") 

## boolean values
# a further data type is bool. There are two possible values:
True
False

# when talking about if- else statements, they will be more important
# for now we just want to present them

has_pets = True

# lastly: input()
# we can ask the user for input via the input function:

name = input()
print(f"Hi {name}!")

# we can add a string/info to the prompt:
# For better formatting we have to add a space or a new line (\n)
name = input("What is your name? ")
print(f"Hi {name}!")

# everthing that the input function returns is a string
# so we may have to convert to the respective type
age = int(input("How old are you? \n> "))
print(f"{age} years old, that's impressive!")
