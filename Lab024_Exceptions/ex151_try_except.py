

a = int(input("enter number 1\t"))
b = int(input("enter number 2\t"))

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error because of zero division, b !=0" )

