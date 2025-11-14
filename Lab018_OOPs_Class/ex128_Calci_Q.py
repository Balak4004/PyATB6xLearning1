
class Calc:
    a = None
    b = None

    def __init__(self):
        print("DC")

    def sum(self,a,b):
        return a+b

    def minus(self,a,b):
        return a-b

    def multi(self,a,b):
        return a*b

    def division(self,a,b):
        return a/b

a = float(input("enter value of a\t"))
b = float(input("enter value of b\t"))

object_ref = Calc()

res_sum = object_ref.sum(a,b)
res_minus = object_ref.minus(a,b)
res_multi = object_ref.multi(a,b)
res_division = object_ref.division(a,b)
print(res_sum,res_minus,res_multi,res_division)