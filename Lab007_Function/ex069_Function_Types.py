
# Type 1 No Return and No Parameter NRNP

def greet():
    print("HI")

greet()

# Type 2 No Return and With parameter

def greet_by_name(name):
    print("Hi,", name)

greet_by_name("Sam")

# Type 3 No return and with default parameter

def default_greet(name="Toni"):
    print("Hi,",name.upper())

default_greet("stark")
default_greet()

# Multiple parameter

def multiple_args(name1="A",name2="B"):
    print("Multiple arguments,", name1,name2)

multiple_args()
multiple_args("Jin","Jan")
multiple_args(name1="Ram")
multiple_args(name1="Jim",name2="Cer")
multiple_args(name2="Roy")

# Type 4 Return with arguments

def sum_of_two(a,b):
    return a + b
result = sum_of_two(4,5)
print(result)


def sum_of_two_numbers_default(num1=100,num2=200):
    print("Sum of two numbers is")
    return num1 + num2

result2 = sum_of_two_numbers_default()
print(result2)

result4 = sum_of_two_numbers_default(20,40)
print(result4)

