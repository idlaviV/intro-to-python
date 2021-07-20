# importing a helper function
from helper import prep_data
#------------------------------------------------------------------------------#
# (1)
# Load the first chapter of harry potter
with open("data/harry_potter_1_chapter_1.txt") as file:
    string_content = file.read()


# After loading pass the string contents to the prep_data function:
data = prep_data(string_content)

# print out the keys for the dictionary
print(data.keys())

# Count the number of mentions of potter and harry in the text.
text = data["text"]
potter_count_1 = text.count("potter")
harry_count_1 = text.count("harry")
text_count = potter_count_1 + harry_count_1
print(f"{potter_count_1=}, {harry_count_1=}, {text_count}")

# Count the number of mentions of potter and harry in the tokens
# using the filter function

tokens = data["tokens"]
token_count = len([*filter(lambda x: x  == "harry" or x == "potter", tokens)])
print(f"{token_count=}")


# write your different results to a json file
result =  {
    "text_count": text_count,
    "token_count": token_count,
}

# normally imports are at the top!
import json

with open("data/count_result.json", "w") as res_file:
    json.dump(result, res_file)
    # res_file.write(json.dumps(result))            # another way

#------------------------------------------------------------------------------#
# (2)
# Write a function which takes a category (of questions - math or sport) and then prompts the
# respective question. Then show the user the different options and 
# let him guess and evaluate his answer.

#this is completely optional
question_enumerate = ["A","B","C","D"]

def read_data():
  try:
    with open("data/quiz.json") as q_file:
        data = json.load(q_file)
        return data
  except Exception as e:
        print(f"Something went wrong: \n{e}")
        return False

def quiz(cat):    
    data = read_data()
    if not data:
      return False    
    categories = list(data["quiz"].keys())
    if not cat.lower() in categories:
        print(f"This quiz has the following categories: {categories}")
        return False

    q_data = data["quiz"]
    questions = q_data[cat]
    q1 = questions["q1"]
    print(q1["question"])
    for index, option in enumerate(q1["options"]):
        print(f"[{question_enumerate[index]}] {option}")
    answer = input("What's your answer: ")
    if answer == q1["answer"] or q1["options"].index(q1["answer"]) == question_enumerate.index(answer):
        print("Correct!")
    else:
        print("Wrong!")
        
        
quiz("maths")
quiz("sport")