

try:
    a = int(input("enter number 1\t"))
    b = int(input("enter number 2\t"))
    c = a / b
    print(c)
except ValueError:
    print("Type error" )
except ZeroDivisionError:
    print("zero div error")
finally:
    print("I will execute !")
