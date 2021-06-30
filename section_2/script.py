
# dynamic creation & list comprehension -> next day

# Lists and Dictinairies
# more types:

## lists are a collection of elements of any type within two [] brackets
friends = ["Ben", "Maria", "Charly"]

meassures = [13, 91, 84, 3.1, 83.4, 65]

# initialize empty list
my_fruits = []

# .append() add new entries / dynamic (for loop -> later)
my_fruits.append("apple")
print(my_fruits)
my_fruits.append("apple")
my_fruits.append("apple")
my_fruits.append("melon")
my_fruits.append("peach")
my_fruits.append("strawberry")
print(my_fruits)

new_fruits = ["pineapple", "banana", "kiwi", "lemon", "kiwi"]

# my_fruits.append(new_fruits)
plus_list = my_fruits + new_fruits
print(plus_list)
my_fruits.extend(new_fruits)
print(my_fruits)

# .count() number of occources of an element
my_fruits.count("apple")

## working with lists: methods & indexing
# .pop() - remove & return the last element - lists needs to be of min len 1
last_el = my_fruits.pop()
print(last_el)
print(my_fruits)

my_fruits.pop()
print(my_fruits)

# alternatively we can also pop a specific element via giving the pop method 
# the index of the to-be-poped item:

my_fruits.pop(0)

# .remove() a specific element
my_fruits.remove("apple")
print(my_fruits)


# when there are multiple identical elements, only the first element gets removed
my_fruits.remove("kiwi")
print(my_fruits)


# .sort() (alpha numeric)
my_fruits.sort()
print(my_fruits)

meassures.sort()
print(meassures)

new_list = meassures + my_fruits
# new_list.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
# conversion of all elements in lists can be achieved 
# using map or list comprehension (later)

# .reverse()
my_fruits.reverse()
print(my_fruits)

# sum
# for lists containing only numbers (ints & floats) we can calculate the sum
# of all values easily using the sum method:
sum_of_meassures = sum(meassures)
print(sum_of_meassures)

print(sum([1,2,3,4,5,6,12]))


## indexing
# first element has index 0, second 1, ...
first = my_fruits[0] # -> returns first element

## last element, cutting & len
# you can cut simply using the :
# cut of first element / return everything after the first element
# the my_fruits list stays the same!
sliced_list = my_fruits[1:]
print(sliced_list)

# cut of everything after the second element
sliced_list = my_fruits[:2]

# so the syntax is [from:to] with the defaults:
# from = 0, to = len(list)-1 (last element)

# get the length of a list:
num_of_fruits = len(my_fruits)

# last index is however:
print(len(my_fruits) - 1)

# .index()
# sometimes you don't know the index of an element, in this case we can use 
# the index() method. The element has to be in the list (not like in JS), else:
# ValueError: 'x' is not in list

# print(my_fruits.index("lemon"))

# if a list contains one fruit/entry multiple times, the index for the first
# occources gets returned (as it's the case for remove())
my_fruits.append("lemon")
print(my_fruits.index("lemon"))


# you can also combine types and create for example an info list for everybody

age = 45
name = "Alex"
info = [age, name, friends]

first_friend = info[2][0]

info2 = [12, "Ben", ["Alex", "Sena", "Leo"]]

all_infos = [info, info2]

second_friend_from_ben = all_infos[1][2][1]

# a little messy -> for structured data & informations we can use dicts, 
# the next thing we will talk about after the exercices

## dicts 
# a dict is a associative list:
# in a list we can access elements via the index ([1]), in a dict we have 
# key: value pirs and access elemts/values using a defined key.
# Syntax is as follows:

personal_info = {"name" : "Tilman"}
print(personal_info)

# for dicts wich hld more than one key-value pair the following 
# is cleaner and clearer.
# and of course we can aso use variables in dicts:
my_job = "student"

personal_info = {
    "name": "Tilman",
    "job": my_job,
    "height": 1.78,
}

print(personal_info)

# often lists of dictionaires are used, where every list entry represents one data point
persons = [
    personal_info,
    {
        "name": "Charly",
        "job": "Teacher",
        "height": 1.68
    }
]

print(persons)

# for naming the keys it is common to use snake_case with all lower chars 
# (as for variables)

# .update()
# if we want to update (add new key:value paires / update existnig) a dict,
# we can use the update method. if the key we specify already exists,
# the method updates, else it appends
personal_info.update({
    "height": 1.69
})
print(personal_info)

personal_info.update({
    "has_pets": True
})
print(personal_info)

personal_info.update({
    "has_pets": False,
    "job": "Taxi Driver"
})

print(personal_info)
# pay attention if you used a variable -> change the values here 
# -> updated everywhere
print(persons)

# todo: pyhton is call by reference?