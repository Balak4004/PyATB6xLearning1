

class Testsuite:
    def info(self):
        print("test suite information")

class Basetest(Testsuite):
    def setup(self):
        print("Base setup")

    def run(self):
        print("run base test")

class Logintest(Basetest):
    def run(self):
        print("run login test")

class APItest(Basetest):
    def run(self):
        print("run API test")

t2 = Logintest()
t2.run()
t2 = APItest()
t2.run()