
# Tuples and Dictionaries 

## tuples
# the difference between lists and tuples ist that tuples are not 
# changeable and values ar within (), they are used 
# to store multiple items in a single variable
coords = (2, 4, 2)
print(type(coords))

# accesing and indicies work the identical to lists
print(coords[0])

# the only methods tuples have are the index and count method we talked about
# for lists. They work identical

print(coords.count(2))

# again, .index() only shows the index of the first found element
print(coords.index(2))

# identical to lists we can also multiply tuples:
print(coords * 2)

## dicts 
# a dict is an associative list:
# in a list we can access elements via the index ([1]), in a dict we have 
# key: value pairs and access elemts/values using a defined key.
# Syntax is as follows:

personal_info = {"name" : "Tilman"}
print(type(personal_info))
print(personal_info)

# for dicts wich hold more than one key-value pair the following 
# is cleaner and clearer.
# and of course we can aso use variables in dicts:
# one important thing: dicts do not allow duplicates!
my_job = "student"

personal_info = {
    "name": "Tilman",
    "job": my_job,
    "height": 1.78,
}

print(personal_info)

# often lists of dictionaires are used, where every list entry represents one data point
# web scraping
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
# if we want to update (add new key:value paires / update existing) a dict,
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

# .get()
# to access the value for a key we can use the get method:
print(personal_info.get("name"))

# alternativly we can use the same syntax we know from lists:
name = personal_info["name"]

my_height = personal_info["height"]
print(f"My height is {personal_info['height']} and my name is {name}!")

# another way to update (similar to lists)
personal_info["height"] = 1.70
print(personal_info)

# .keys()
# sometimes you may need all existing keys for a dict, you can get those 
# via the keys method:
print(personal_info.keys())
