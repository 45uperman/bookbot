def wordcount(text):
    words = text.split()
    return words
def gettext(name):
    book = f"books/{name}.txt"
    return open(book).read()

filename = input("Which book would you like to look at?\n")
filecontent = gettext(filename)
print(f"There are {wordcount(filecontent)} words in {filename}!")
more = input("Would you like to know more? [y/n]\n")
if more == "y":
    pass

