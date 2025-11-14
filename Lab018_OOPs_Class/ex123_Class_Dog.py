from Lab016_Filter.ex111_filters3 import names


class Dog:
    # Attribute
    name = None
    breed = None
    height = None
    weight = None

    # Behaviour
    def bark(self):
        print("barking")
        # print(name)
        print(self.name)

    def eat(self):
        print("eating")


tomy = Dog()
bandi = Dog()
# Dog() is object
# tomy object reference

tomy.bark()
bandi.eat()


