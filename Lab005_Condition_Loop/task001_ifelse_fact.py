'''
Given a Number a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1

'''
num = int(input("enter the num : "))
fact = 1

if num < 0:
    print("Number is negative, Enter positive number")
elif num == 0:
    print("factorial of 0 is : ", fact)
else:
    for i in range(1,num+1):
        fact = fact * i
    print("factorial of ",num, "is : ", fact)







'''
num = int(input("enter the num : "))
fact = 1

if num == 0:
    fact = 1
else:
    for i in range(1,num+1):
        fact = fact * i
print("factorial of number : ",num, "is : ", fact)
'''