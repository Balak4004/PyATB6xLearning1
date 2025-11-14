
class Person:

    name = None
    age = None
    height = None
    weight = None
    city = None

    def __init__(self):
        self.name = "amit"
        self.age = 18
        self.height = "5ft 10 inch"
        self.weight = "45.66kg"
        self.city = "Delhi"

    def p_name(self):
        return self.name

    def p_age(self):
        return self.age

    def p_height(self):
        return self.height

    def p_weight(self):
        return self.weight

    def p_city(self):
        return self.city

object_ref = Person()
print(object_ref.p_name())
print(object_ref.p_age())
print(object_ref.p_height())
print(object_ref.p_weight())
print(object_ref.p_city())
