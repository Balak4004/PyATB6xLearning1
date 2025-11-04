

#Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
#i/p - int side1 == side2 =side3 → isoceles
#side1==side2==side3 -> equilateral triangle
#side1==side2 or side1==side3 or side2==side3 -> isosceles triangle
#o/p = result in string - iso, eq, scalene

side1=int(input("enter length of side1 : "))
side2=int(input("enter length of side2 : "))
side3=int(input("enter length of side3 : "))

def traingle_type(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            if a == b == c:
                return "equilateral triangle"
            elif side1==side2 or side1==side3 or side2==side3:
                return "isosceles triangle"
            else:
                return "scalene triangle"
        else:
            print("Not a triangle")
    else:
        print("enter valid length")

result = traingle_type(side1,side2,side3)
print(result)

'''
side1=int(input("enter length of side1 : "))
side2=int(input("enter length of side2 : "))
side3=int(input("enter length of side3 : "))

def traingle_type(side1,side2,side3):
    if side1<=0 or side2<=0 or side3<=0:
        print("enter valid value")
    elif side1 == side2 and side2 == side3:
        print("equilateral triangle")
    elif side1==side2 or side1==side3 or side2==side3:
        print("isosceles triangle")
    else:
        print("scalene triangle")

traingle_type(side1,side2,side3)
'''

'''
def traingle_type(side1,side2,side3):
    if side1<=0 or side2<=0 or side3<=0:
        print("enter valid value")
    elif side1 == side2 and side2 == side3:
        print("equilateral triangle")
    elif side1==side2 or side1==side3 or side2==side3:
        print("isosceles triangle")
    else:
        print("scalene triangle")

traingle_type(side1=int(input("enter length of side1 : ")),
              side2=int(input("enter length of side2 : ")),
              side3=int(input("enter length of side3 : ")))
'''