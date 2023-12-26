import string

def gettext(name):
    book = f"books/{name}.txt"
    return open(book).read()
def wordcount(text):
    words = text.split()
    return len(words)
def lettercount(text, letter):
    letters = text.split(letter)
    return len(letters)

filename = input("Which book would you like to look at?\n")
filecontent = gettext(filename)
print(f"There are {wordcount(filecontent)} words in {filename}!")
more = input("Would you like to know more? [y/n]\n")
if more != "y":
    exit
letterenumeration = ""
for i in string.ascii_lowercase:
    letterenumeration = f"{letterenumeration}The letter '{i}' appears {lettercount(filecontent.lower(), i)} times.\n"
print(letterenumeration)