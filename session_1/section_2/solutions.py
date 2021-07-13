
# ca 15-20 min

#------------------------------------------------------------------------------#
# (1)
# create a new list containing at least 5 values (ints or floats)

values = [15,2.12,3,84,99,12,8.1]

# create a second list containing min. 2 values and extend your first list
more_values = [237, 1564]
values.extend(more_values)


# get the sum of the largest two values
values.sort()
sum_2_large = sum(values[-2:])
print(sum_2_large)
# or:
values.reverse()
other_sum_2_large = values[:2]
print(other_sum_2_large)


#------------------------------------------------------------------------------#
# (2)
# print the last element of the names list without using reverse
names = ["Tilman", "Clara", "Maria", "Iven", "Emma", "Mo"]
print(names[-1])
print(names[len(names)-1])


# remove Emma from the list without writing Emma
index_emma = names.index("Emma")
names.pop(index_emma)
print(names)

names = ["Tilman", "Clara", "Maria", "Iven", "Emma", "Mo"]
names = names[:4] + [names[-1]]
print(names)

names = ["Tilman", "Clara", "Maria", "Iven", "Emma", "Mo"]
last = names[-1]
names = names[:4]
names.append(last)
print(names)


# remove the third name without using the index
 
print(names)