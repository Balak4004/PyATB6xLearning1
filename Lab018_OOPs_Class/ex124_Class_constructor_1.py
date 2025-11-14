
print("outside the class")

class Mobile:
    model = None

    # default constructor __init__
    def __init__(self):
        print("default constructor")        #printed without calling

    def talk(self):
        print("Hi talking")

    def UI(self,name):
        print(name,"smooth")


iphone = Mobile()
iphone.talk()
iphone.UI("Iphone17")

print("outside the class2")