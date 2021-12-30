# factorial
n = int(input("Enter a number: "))
copy = n
f = 1

while n > 0:
    f = f * n
    n = n - 1

print("factorial of", copy, "is", f)
