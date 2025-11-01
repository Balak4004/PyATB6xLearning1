


# SUm of three numbers from user input
# if user doesnt enter any number take 100, 200, 300

#num1 = int(input("enter the first number\t"))
#num2 = int(input("enter the second number\t"))
#num3 = int(input("enter the third number\t"))

def sum_of_three_num(n1=100,n2=200,n3=300):
    return n1 + n2 + n3

result11 = sum_of_three_num(3,4,5)
print(result11)
result12 = sum_of_three_num()
print(result12)
result13 = sum_of_three_num(n1=10)
print(result13)
result14 = sum_of_three_num(n1=10,n2=20)
print(result14)
result15 = sum_of_three_num(n2=10)
print(result15)
result16 = sum_of_three_num(n3=10)
print(result16)

#result16 = sum_of_three_num(n3=num3)
#print(result16)









'''
num1 = int(input("enter the first number\t"))
num2 = int(input("enter the second number\t"))
num3 = int(input("enter the third number\t"))

def sum_of_three_num(n1=100,n2=200,n3=300):
    return n1 + n2 + n3

result5 = sum_of_three_num(num1,num2,num3)
print(result5)
'''