# file = open("textfile.txt")
# text = file.read()
# file.close()
# print(text)

# Better way to read file sing with keywords

with open("textfile.txt") as file
    text = file.read()
    print(text)