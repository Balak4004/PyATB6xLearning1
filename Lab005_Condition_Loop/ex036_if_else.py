
# verify the user age

'''
age = int(input("enter the age :\n"))
if age>=21:
    print("You can vote")
else:
    print("you can't vote")
'''

# optimized code
age = int(input("enter the age :\n").strip())

if age <= 0 or age > 130:
    print("enter a valid age")
else:
    if age>=21:
        print("You can vote")
    else:
        print("you can't vote")
