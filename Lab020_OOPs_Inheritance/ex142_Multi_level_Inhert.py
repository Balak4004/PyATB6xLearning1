

class Testsuite:
    def info(selfse):
        print("This is - GF - step 1")
class Basetest(Testsuite):
    def setup(self):
        print("Base test - F - step 2")
class UItest(Basetest):
    def run(self):
        self.info()
        self.setup()
        print("Running test case - S - step 3")

d1 = UItest()
d1.run()
