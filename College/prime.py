# prime number
import math

n = int(input("Enter a number: "))

i = 1
c = 0

while i <= math.sqrt(n):
    if n % i == 0:
        c = c + 1
    i = i + 1


if c == 1:
    print(n, "is prime")
else:
    print(n, "is composite")


