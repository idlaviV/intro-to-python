
def prep_data(str_cont):
    str_cont = str_cont.lower()
    ps = str_cont.split("\n")
    text = " ".join(ps)
    tokens = " ".join(text.split(";"))
    tokens = " ".join(tokens.split("'"))
    tokens = " ".join(tokens.split("\""))
    tokens = " ".join(tokens.split("-"))
    tokens = " ".join(tokens.split(","))
    tokens = " ".join(tokens.split("."))
    tokens = " ".join(tokens.split("  "))
    tokens = tokens.split(" ")
    return {
        "text": text,
        "tokens": tokens,
        "paragraphs": ps
    }
    

# def load_data():
#     content = ""
#     with open("data/harry_potter_1_chapter_1.txt") as f:
#         content = f.read()
#     return prep_data(content)