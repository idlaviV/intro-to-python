# ------------------------------------------------------------------------------#
# (1) 
# hint
s = "Hallo"
print(s.lower())
names = ["Tilman", "Clara", "Maria", "Iven", "Emma", "Mo"]

# Lower all names in the names list
names = [str.lower, names]
print(names)


# Filter all names which include 2 'a':
def count_a(string):
    i = 0
    for sym in string:
        if sym == "a":
            i += 1
    return i


names = [*filter(lambda x: count_a(x) < 2, names)]
print(names)


# ------------------------------------------------------------------------------#
# (2) 
# Create a class for traffic light and come up with two properties.
# Implement a method for phase switching

class Light:
    def __init__(self, on_off, location, status=True):
        self.on_off = on_off
        self.location = location
        self.status = status

    def switch(self):
        self.on_off = not self.on_off

    def to_string(self):
        if self.status:
            if self.on_off:
                print(f"The traffic light on {self.location} is showing green.")
            else:
                print(f"The traffic light on {self.location} is showing red.")
        else:
            print(f"The traffic light on {self.location} is broken.")


# Init a traffic light object and switch the phase 2 times
my_traffic_light = Light(True, "Kaiserstraße")
my_traffic_light.to_string()
my_traffic_light.switch()
my_traffic_light.to_string()
Light.switch(my_traffic_light)
Light.to_string(my_traffic_light)
