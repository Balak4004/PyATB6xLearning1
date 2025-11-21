

# Multiple Inherit -- subclass have more than one parent

class Father1:

    def money(self):
        print("F1 money")

class Father2:

    def money(self):
        print("F2 money")

class Child(Father1,Father2):
#class Child(Father2, Father1):
    def give_money(self):
        print("son")
        self.money()

c1 = Child()
c1.give_money()