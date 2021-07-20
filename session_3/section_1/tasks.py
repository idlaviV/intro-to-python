# importing a helper function
import json

from helper import prep_data

# ------------------------------------------------------------------------------#
# (1)
# Load the first chapter of harry potter

DIRECTION = "data/harry_potter_1_chapter_1.txt"
with open(DIRECTION, "r") as stream:
    string_content = stream.read()

# After loading pass the string contents to the prep_data function:
data = prep_data(string_content)

# print out the keys for the dictionary

print(data.keys())

# Count the number of mentions of potter and harry in the text.
text = data["text"]
harry_text = text.count("harry")
potter_text = text.count("potter")
print(harry_text)
print(potter_text)

# Count the number of mentions of potter and harry in the tokens
# using the filter function
potter_tokens = (len([*filter(lambda x: x == "potter", data["tokens"])]))
harry_tokens = (len([*filter(lambda x: x == "harry", data["tokens"])]))


# write your different results to a json file
results = {
    "text": {
        "number_of_potter_in_text": potter_text,
        "number_of_harry_in_text": harry_text
    },
    "tokens": {
        "number_of_potter_in_tokens": potter_tokens,
        "number_of_harry_in_tokens": harry_tokens
    }
}

new_json_file = "data/results_of_count.json"
with open(new_json_file, "w") as file:
    json.dump(results, file)


# ------------------------------------------------------------------------------#
# (2)
# Write a function which takes a category (of questions - math or sport) and then prompts the
# respective question. Then show the user the different options and 
# let him guess and evaluate his answer.
questions_file = "data/quiz.json"
with open(questions_file, "r") as file:
    import_file = json.load(file)

quiz = import_file["quiz"]
while True:
    print("Please pick one of the following categories:")
    for key in quiz.keys():
        print("* " + key)
    user_input = input(">")
    if user_input == "q":
        break
    try:
        category = quiz[user_input]
        questions = quiz[category]
        # for i in range(len(questions)):
            # print(questions)
    except Exception as e:
        print("Illegal category.")
