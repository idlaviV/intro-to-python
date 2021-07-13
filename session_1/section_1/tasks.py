# ca. 10-15 min

# ------------------------------------------------------------------------------#
# (1)
# convert the value to a float and round it to the next thousand
value = "999.15"
print(round(float(value), -3))

# print out the string within <>: <"I don't know.", he said. "What you think?">
print("\"I don't know.\", he said. \"What you think?\"")
# ------------------------------------------------------------------------------#
# (2)
# Create new variables for: your name, age and one hobby
your_name = "Leonid"
age = 42
hobby = "Creating messy python code"
# print out a sentence containing all of your information
print(f"My name is {your_name}, I\'m {age} years old. {hobby} is one of my hobbies.")

# For the nex task, we have a carpool with 100 cars, in every car
# there are 4 available seats. In total we have 30 drivers and 90 passengers
# compute the carpool capacity (how many people can be transported),
# the average passengers per car, the number of empty cars and print out the results
cars = 100
seats = 4
drivers = 30
passengers = 90

carpool_capacity = min(cars, drivers) * seats
average_passengers = max(passengers / cars, 0)
empty_cars = max(cars - drivers, 0)

print(f"Carpool capacity: {carpool_capacity}")
print(f"Average passengers: {average_passengers}")
print(f"Empty cars: {empty_cars}")

# as an addition make the total number of cars, available seats, driver and 
# passengers dependent on user input
cars = int(input("Input number of cars:\n >"))
seats = int(input("Input number of seats per car:\n >"))
drivers = int(input("Input number of drivers:\n >"))
passengers = int(input("Input number of passengers:\n >"))


carpool_capacity = min(cars, drivers) * seats
if cars != 0:
    average_passengers = max(passengers / cars, 0)
else:
    average_passengers = "No cars available!"

empty_cars = max(cars - drivers, 0)

print(f"Carpool capacity: {carpool_capacity}")
print(f"Average passengers: {average_passengers}")
print(f"Empty cars: {empty_cars}")

# ------------------------------------------------------------------------------#
# (3)
# Fix the errors in the following lines in any way you like
age = 12
print(f"\'My age is {age} and this isn\'t a problem\'")

print("""This is the last task in this 
exercise section!""")
