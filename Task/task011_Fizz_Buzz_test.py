
# print numbers between 1 to 100
# print Fizz for multiple of 3
# print Buzz for multiple of 5
# print FizzBuzz for multiple of both 3 & 5


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
    elif i % 3 == 0:
        print("Fizz", i)
    elif i % 5 == 0:
        print("Buzz", i)
    else:
        print(i)