

class Basetest:
    def setup(self):
        print("setup from Base test")

class Logintest(Basetest):
    def run(self):
        print("Running login test")

class Signuptest(Basetest):
    def run(self):
        print("Running the signup test")

Logintest().setup()
Logintest().run()
Signuptest().setup()
Signuptest().run()