# ca 10 min

# ------------------------------------------------------------------------------#
# (1)
# Create a dictionary with (made-up) information about you.
# Include a list of friends and a key:value pair with a dictionary as a value
# for the names of family members and their "role" (brother, mother, ...)

my_info = {
    "name": "Hans Meier",
    "mother": "Gerda Meier",
    "brother": "Felix Meier",
    "father": "Siegfried Meier",
    "grandmother": "Sieglinde Meier",
    "friends": ["Adam", "Boris", "Carsten", "Deborah", "Esma"],
    "age": 42
}

# ------------------------------------------------------------------------------#
# (2)
# print out the name of one of your relatives and their role like this:
# My <role>'s name is <name>.

role = "mother"
print(f"My {role}'s name is {my_info[role]}.")

# remove one friend and add two new ones

print(my_info)

my_info.pop("grandmother")
print(my_info["friends"])
my_info["friends"].remove("Adam")
my_info["friends"].append("Kain")

print(my_info)
# change one value (e.g. your name, age, ...)

my_info.update({"age": my_info["age"] + 1})

print(my_info)
