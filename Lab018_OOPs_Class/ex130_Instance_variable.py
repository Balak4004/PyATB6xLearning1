

a = 10      # variable everywhere

class Person:

    b = 12      # instance variable

    def print_info(self):
        c = 20      # local variable
        print(c)
        print(self.b)
        print(a)


object_ref = Person()
print(a)
print(b)
print(c)