

class Calc:
    a = None
    b = None

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b

    def minus(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


object_ref = Calc(5,3)

res_sum = object_ref.sum()
res_minus = object_ref.minus()
res_multi = object_ref.multi()
res_division = object_ref.division()
print(res_sum,res_minus,res_multi,res_division)