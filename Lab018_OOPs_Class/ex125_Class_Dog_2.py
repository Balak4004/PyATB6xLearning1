

class Dog:
    # Attribute
    name = None
    breed = None
    height = None
    weight = None
    race = None

    # convert init as parameterized constructor
    def __init__(self,name,breed):
        print("parameterized constructor")
        self.name = name
        self.breed = breed


    def bark(self):
        print("barking")

    def sleep(self):
        print("who is sleeping",self.name)

    def talk(self):
        pass

tomy = Dog("tomy","mastiff")
bandi = Dog("bandi","desi")

tomy.sleep()
bandi.sleep()