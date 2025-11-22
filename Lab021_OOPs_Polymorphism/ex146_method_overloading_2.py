

class Mathclass:
    def add(self,a,b):
        return a + b 

    def add(self, a, b, c=10):
        return a + b + c

obj1 = Mathclass()
print(obj1.add(3,4,5))
print(obj1.add(3.14,4.14))
