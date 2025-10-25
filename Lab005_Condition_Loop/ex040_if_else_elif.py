

# find max of three numbers -> 5,3,2

num1 = float(input("enter first number : ").strip())
num2 = float(input("enter second number ; ").strip())
num3 = float(input("enter third number : ").strip())

if num1 >= num2 and num1 >= num3:
    print('max number is : ', num1)
elif num2 >= num1 and num2 >= num3:
    print('max number is : ', num2)
else:
    print("max number is : ", num3)