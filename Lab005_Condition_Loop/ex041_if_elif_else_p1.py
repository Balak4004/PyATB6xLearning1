
# grade calculator
# A 90 - 100
# B 80 - 89
# C 70 - 79
# D 60 - 69
# F 0 - 59


num1 = float(input("enter the number ; ").strip())

if num1 < 0 or num1 > 100:
    print("enter valid number")
else:
    if num1 >= 90 and num1 <= 100:
        print("Grade A")
    elif num1 >= 80 and num1 <= 89:
        print("Grade B")
    elif num1 >= 70 and num1 <= 79:
        print("Grade C")
    elif num1 >= 60 and num1 <= 69:
        print("Grade D")
#elif num1 >= 0 and num1 <= 59:
    else:
        print("Grade F")
