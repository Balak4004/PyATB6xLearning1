
# find max of 2 numbers

num1 = float(input("enter first number \n").strip())
num2 = float(input("enter second number \n").strip())

#if num1 > 0 and num2 > 0:       # ask from interview num should be positive or not
if num1 >= num2:
        print("max number is : ",num1)
else:
        print("max number is : ", num2)
#else:
#    print("enter positive number")