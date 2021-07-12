## Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Indent is important! (Tab)

def hello():                # function head
    print("Hello")          # function body
    

hello()                     # call/execute the function

## Arguments
# Information can be passed into functions as arguments/parameters.
def hello(name):
    print(f"Hello {name}!")
    
hello("Tilman")
hello("Sarah")

# we can use any number of arguments:
def hello(fname, lname):
    print(f"Hello {fname} {lname}!")
    
hello("Tilman", "Kerl")

# however when you have a lot of info to pass use lists, dicts or 
# arbitrary arguments: *args
# args is a list
def mmin(*args):
    min_value = 999999
    for value in args:
        if value < min_value:
            min_value = value
    return min_value    # we can use the return statement to return 
                        # the result of the function

print(mmin(59,152))
print(mmin(132,12,141))

# This however will throw an error:
# print(mmin([98,53,756,23,-99]))

# We can adjust our function:
def mmin(*args):
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    min_value = 999999
    for value in args:
        if value < min_value:
            min_value = value
    return min_value

print(mmin([98,53,756,23,-99]))


## Default args:
def hello(name, lang="en"):
    if lang == "fr":
        print(f"Salut {name}")
    elif lang == "de":
        print(f"Hallo {name}")
    else:
        print(f"Hello {name}")
        
# call the function        
hello("Tilman")
hello("Tilman", "de")
hello("Tilman", lang="de")


## Recursion
# A function can call itself - recursion
# whenever we use this, we need a break condition!

# one easy example:
def fib(prev1=0, prev2=1, stop=10):
    if prev2 >= stop:
        return 1
    if prev1 == 0:
        print(prev1)
        print(prev2)
    new_value = prev1 + prev2
    print(new_value)
    fib(prev2, new_value, stop=stop)
    
    
fib()
    

