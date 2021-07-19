
## Working with files
# Reading data 

DATA_DIR = "data"
# DRY!
mkf = lambda f: f"{DATA_DIR}/{f}"

filename = "harry_potter_1_chapter_1.txt"
file = mkf(filename)

f_stream = open(file, "r")
content = f_stream.read()
print(content[:100])
print(content.count("Harry"))

first_100_chars = f_stream.read(100)
print(first_100_chars)

# read one line:
print(f_stream.readline())

# loop through every line:
for line in f_stream:
    print(line)

# always close file streams - good practice!
f_stream.close()

# or use with statement to take care of this:
with open(file, "r") as stream:
    file_content = stream.read()
    
    
# but even with the 'with statement' there might be errors, e.g. file not found
# in order to handle such problems we can use try, except:
err_file = "this_file_does_not_exist"
try:
    with open(err_file, "r") as stream:
        file_content = stream.read()
except Exception as e:
    # with raise we can raise/throw the error and abort the programm
    # raise e
    # alternativly we can log the event and inform the user:
    print(f"An error occured while opening the file <{err_file}>: \n{e}")

# we have different modes when opening files:
# r - read
# w - write 
# a - append
# x - create

# we can add an additional value:
# t - text mode 
# b - binary mode (e.g. images)

# Writing data then works as aspected:
empty_filename = "empty_file.txt"
empty_file = mkf(empty_filename)
with open(empty_file, "w") as fi:
    fi.write("Hello my name is Tilman!")
    
# let's check if it worked:
with open(empty_file, "r") as fi:
    print(fi.read())
    
    
# writing to non-exiting files:
new_filename = "a_new_file.txt"
new_file = mkf(new_filename)
with open(new_file, "w") as fi:
    fi.write("A fresh start in a new file.")


## when working with data we often run into two different types of files:
# JSON: JavaScript Object Notation
# We have key-value pairs similar to dictionaries
# For more on JSON see: 
# https://www.json.org/ (including formal definition/grammar)
# Main difference between JSON & dicts: 
# JSON is a string with a specific structure
# we can load json using the json package
# normally package imports are at the top of the file!
import json

# we have to options when loading a json file:
# 1. read the file as text and the convert it to json (json.loads())
with open("data/example.json", "r") as example_file:    
    data = json.loads(q_file.read(q_file))


# 2. or read it directly as json (json.load())
with open("data/example.json", "r") as example_file:    
    data = json.load(example_file)

data["users"].append({
  "userId": 111,
  "firstName": "Tilman",
  "lastName": "Kerl",
  "phoneNumber": "+49123456",
  "emailAddress": "tilman.kerl@uni.kn"
})

# the same logic holds for writing - here the methods are .dump() and .dumps():
with open("data/example.json", "a") as example_file:
    json.dump(data, example_file)
    # or:
    example_file.write(json.dumps(data))            # another way
