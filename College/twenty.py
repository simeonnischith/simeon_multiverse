#  20th program - reverse a string
stringofwords = input("Enter a string: ")
listofwords = stringofwords.split()

listofwords.reverse()

stringfinal = ""

for i in listofwords:
    stringfinal += i+" "

print(stringfinal)
