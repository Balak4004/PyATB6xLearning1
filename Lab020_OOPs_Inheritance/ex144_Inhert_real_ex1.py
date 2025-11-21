
class Basetest:
    def __init__(self,browser):
        self.browser = browser

    def setup(self):
        print(f"launching browser {self.browser}")


class Logintest(Basetest):
    def run_test(self):
        self.setup()
        print("running login test case")

class Signuptest(Basetest):
    def run_test(self):
        self.setup()
        print("running sign up test case")

t1 = Logintest("chrome")
t1.run_test()

t1 = Logintest("edge")
t1.run_test()

