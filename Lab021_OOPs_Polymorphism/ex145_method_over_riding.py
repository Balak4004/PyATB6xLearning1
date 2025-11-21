

class Basetest:
    def run(self):
        print("running the generic test")

class Logintest(Basetest):
    def run(self):
        print("running the login test case")

t1 = Logintest()
t1.run()

t1 = Basetest()
t1.run()