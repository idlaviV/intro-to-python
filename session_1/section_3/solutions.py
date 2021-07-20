
# ca 15-20 min

#------------------------------------------------------------------------------#
# (1)
# Create a dictionary with (made-up) informations about you.
# Include a list of friends and a key:value pair with a dictionary as a value
# for the names of family members and their "role" (brother, mother, ...)

my_info = {
    "name": "Tilman",
    "job": "student",
    "pets": False,
    "friends": ["Emma", "Sarah", "Sena", "Iven", "Anton"],
    "family": {
        "brother": "Kilian",
        "mother": "Imke",
        "father": "Jörn",
    }
}  
print(my_info)


#------------------------------------------------------------------------------#
# (2)
# print out the name of one of your relatives and their role like this:
# My <role>'s name is <name>.

print(f"My brother's name is {my_info['family']['brother']}")

# remove one friend and add two new ones

my_info["friends"].pop()
my_info["friends"] += ["Mo", "Leonie"]
print(my_info)

# change one value (e.g. your name, age, ...)
my_info["pets"] = False
print(my_info)
