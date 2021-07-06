# ca 15-20 min
import sys

# ------------------------------------------------------------------------------#
# (1)
# create a new list containing at least 5 values (ints or floats)
list_of_values = [2, 3.5, 0, 9223372036854775807 ** 4, 4345, 2.5 ** 14, -3, -125.1244]
print(list_of_values)


# create a second list containing min. 2 values and extend your first list
another_list = [0, 0, 0, 1]
list_of_values.extend(another_list)

# get the sum of the largest two values
# version 1
safe_copy = list_of_values.copy()
safe_copy.sort()
value1 = safe_copy.pop()
value2 = safe_copy.pop()
print(f"Values are {value1}, {value2}")
print(f"Sum of max values {value1 + value2}")


# version 2
safe_copy = list_of_values
max_value = max(safe_copy)
safe_copy.remove(max_value)
max2_value = max(safe_copy)
print(f"Values are {max_value}, {max2_value}")
print(f"Sum of max values {max_value + max(safe_copy)}")

# ------------------------------------------------------------------------------#
# (2)
# print the last element of the names list without using reverse
names = ["Tilman", "Clara", "Maria", "Iven", "Emma", "Mo"]
print(names[len(names)-1])
print(names[-1])

# remove Emma from the list without writing Emma
names.pop(4)
print(names)

# remove the third name without using the index
names.remove("Maria")
print(names)
