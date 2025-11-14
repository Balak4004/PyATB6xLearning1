
class Dog:
    # Attribute
    name = None
    breed = None
    height = None
    weight = None


    def __init__(self):
        print("I will be called")

    def bark(self):
        print("barking")

    def sleep(self):
        print("who is sleeping",self.name)

    def talk(self):
        pass

tomy = Dog()    # calls default constructor
bandi = Dog()   # calls default constructor

print(tomy.name)
print(bandi.name)