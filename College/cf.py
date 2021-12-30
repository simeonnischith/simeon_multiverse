# Program to convert temperatures from Celsius to Fahrenheit
try:
    temp = input("Enter the temperature: ")
    value = int(temp[:len(temp)-1].strip())
    unit = temp[len(temp)-1].upper()

    if unit == "F":
        print((5*(value-32))/9, "C")
    elif unit == "C":
        print((9*value/5) + 32, "F")
    else:
        print("Recheck units")
except:
    print("Invalid Entry")
