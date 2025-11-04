
# Leap year if multiple of 4 and not multiple of 100

# Leap year is multiple of 400

year = int(input("enter the year:\t"))

def check_leap_year():
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False

result = check_leap_year()
print(result)


