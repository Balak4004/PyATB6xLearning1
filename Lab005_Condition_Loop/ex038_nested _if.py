
# find number is even or odd


num1 = float(input("enter the number : ").strip())

if num1 > 0:
    if num1 % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is negative")