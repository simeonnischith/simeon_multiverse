# armstrong
n = int(input("Enter a number: "))
s = 0
copy = n

while n > 0:
    s += (n % 10) ** 3
    n = int(n / 10)

if copy == s:
    print(copy, "is Armstrong")
else:
    print(copy, "is not Armstrong")




