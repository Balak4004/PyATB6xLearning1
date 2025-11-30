
class InvalidAgeException(Exception):
    pass

def can_you_drink(age):
    if age <18:
        print("yes, you can drink")
        raise InvalidAgeException("Invalid age of drinking")

can_you_drink(17)
can_you_drink(24)


# builtin exception

def zero_div_error(a):
    if a == 0:
        raise ZeroDivisionError("cannot divide with zero")

zero_div_error(0)