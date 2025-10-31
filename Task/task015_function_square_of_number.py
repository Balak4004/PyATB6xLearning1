'''
 Create a function which will take a positive number from the user and perform square of the number?

i/o = 3
o/p = 9
'''

num=int(input("enter number : "))

def square_of_number(num):
    if num > 0:
        print(num**2)
    else:
        print("Enter positive number")

square_of_number(num)


'''
def square_of_number(num):
    if num > 0:
        #print(num**2)
        return num**2
    else:
        print("Enter positive number")


result  = square_of_number(num=int(input("enter number : ")))
print(result)
'''