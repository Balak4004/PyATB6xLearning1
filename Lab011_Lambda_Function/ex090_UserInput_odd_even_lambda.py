

num1 = int(input("enter the number:\t"))

check_even_odd_func = lambda num1:"Even" if num1%2==0 else "Odd"
result = check_even_odd_func(num1)
print(result)