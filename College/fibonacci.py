# fibonacci


def fib(n):
    if n == 1:
        print("0 ")

    elif n == 2:
        print("0 1 ")

    else:
        print("0 1 ", end="")

        a = 0
        b = 1

        i = 1

        while i <= (n-2):
            c = a + b
            print(c, end=" ")
            a = b
            b = c
            i = i + 1



