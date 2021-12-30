# 13th program - check if triangle is a right angle triangle

a = int(input("Enter side A of the triangle: "))
b = int(input("Enter side B of the triangle: "))
c = int(input("Enter side C of the triangle: "))

A = max(a, b, c)
B = min(a, b, c)
C = (a + b + c) - (A + B)

if A*A == (B*B+C*C):
    print("Triangle is right angled")
else:
    print("Triangle is not right angled")



