# file = open("text.txt", "r")
# x = file.read()
# print(x)
# file.close


word = input("enter word you need to add")
with open ("/Users/mac/Documents/All progects/py pro/text.txt", "a") as file:
    file.write(word)


with open ("text.txt", "r") as file:
    x = file.read()
print(x)