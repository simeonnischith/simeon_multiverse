# power


def pow(x, n):
    return (x**n)


number = int(input("Enter a number: "))
power = int(input("Enter the power to be raised: "))

print(number, "power ", power, " = ", pow(number, power))
