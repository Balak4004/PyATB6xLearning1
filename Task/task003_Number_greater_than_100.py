
# Write a program to check if a number entered by the user is greater than 100.

num = int(input("Enter the number : "))

if num < 0 :
    print("Enter positive number")

elif num < 100:
        print(num, "is less than 100")

elif num == 100:
    print(num, "is equal to 100")
else:
    print(num, "is greater than 100")
