
# ca. 10-15 min

#------------------------------------------------------------------------------#
# (1)
# convert the value to a float and round it to the next thousand
value = "999.15"

value = float(value)
value = round(value, -3)
print(value)

# print out the string within <>: <"I don't know.", he said. "What you think?">
print("I don't know.\", he said. \"What you think?\"")
print('I don\'t know.", he said. "What you think?"')

print(20*"-")
#------------------------------------------------------------------------------#
# (2)
# Create new variables for: your name, age and one hobby
name = "Tilman"
age = 22
hobby = "handball"

# print out a sentence containing all of your information
print(f"My name is {name}, I am {age} years old and like to play {hobby}")

print(20*"-")
# For the nex task, we have a carpool with 100 cars, in every car 
# there are 4 available seats. In total we have 30 drivers and 90 passangers
# compute the carpool capacity (how many people can be transportet), 
# the average passengers per car, the number of empty cars and print out the results

cars = 100
available_seats = 4
drivers = 30
passengers = 90

carpool_capacity = drivers * available_seats
average_passengers_per_car = passengers / drivers
empty_cars = cars - drivers
print(f"The total capacity is: {carpool_capacity}")
print(f"There are in {average_passengers_per_car} passengers in every car in average")
print(f"There are {empty_cars} empty cars")


print(20*"-")
# as an addition make the total number of cars, available seats, driver and 
# passengers dependent on user input
cars = int(input("How many cars are in the carpool? "))
available_seats = int(input("How many seats are available in every car?"))
drivers = int(input("How many drivers are there? "))
passengers = int(input("How many passengers are there? "))

carpool_capacity = drivers * available_seats
average_passengers_per_car = passengers / drivers
empty_cars = cars - drivers
print(f"The total capacity is: {carpool_capacity}")
print(f"There are in {average_passengers_per_car} passengers in every car in average")
print(f"There are {empty_cars} empty cars")


print(20*"-")
#------------------------------------------------------------------------------#
# (3)
# Fix the erros in the following lines in any way you like
age = 12
# print('My age is " + age " and this isn't a problem')
print(f'My age is {age} and this isn\'t a problem')
# print('My age is ' + str(age) + ' and this isn\'t a problem')

# print("This is the last task in this 
# exercise section!")

print("""This is the last task in this 
exercise section!""")
# print("This is the last task in this" 
# + "exercise section!")
# print("This is the last task in this exercise section!")

