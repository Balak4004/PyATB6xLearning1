

try:
    a = int(input("enter number 1\t"))
    b = int(input("enter number 2\t"))
    c = a / b
    print(c)
except (TypeError,NameError,ValueError, ZeroDivisionError):
    print("Error due to the Type, Name, value, zero div" )

