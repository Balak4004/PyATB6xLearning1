
# Single Inheritance
# A subclass/child inherits from parent/base


class BaseTest:
    driver = "chrome"
    __driver2 = "Firefox"

    def setup(self):
        print(f"Base setup with browser and env with {self.__driver2}")

class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print(f"Running the Testcases in {self.driver} browser")

t = LoginTest()
t.run()