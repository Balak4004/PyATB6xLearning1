
#import math

#math.pi

radius = float(input("enter radius :\n"))
print(radius)

area = 3.14987654 * (radius ** 2)
area1 = 3.14987654 * (pow(radius,2))

print("area of circle :", area)
print("area of circle :", area1)

print(f"area of circle : {area:.2f}")
print(f"area of circle : {area1:.2f}")