

try:
    a = int(input("enter number 1\t"))
    b = int(input("enter number 2\t"))
    c = a / b
except ValueError:
    print("Type error" )
except ZeroDivisionError:
    print("zero div error")
else:   # Runs only if try block succeeds
    print(c)
finally:
    print("I will execute !")
