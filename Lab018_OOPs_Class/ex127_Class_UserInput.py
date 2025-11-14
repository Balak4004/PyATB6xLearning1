

class Person:
    name = None
    age = None
    city = None

    def __init__(self):
        print("lets take user input")
        self.name = input("enter name\t")
        self.age = int(input("enter age\t"))
        self.city = input("enter the city name\t")

    def display_values(self):
        print("name is", self.name, "age is ",self.age,"living in city ",self.city)


amit = Person()
amit.display_values()