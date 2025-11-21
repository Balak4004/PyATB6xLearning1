

class BaseTest:
    _driver = "chrome"

    def setup(self):
        print(f"launching browser {self._driver}")


class Logintest(BaseTest):
    __username = "admin123"
    __password = "pass@123"

    def get_user(self):
        return self.__username

    def run_test(self):
        user = self.get_user()
        print(f"running the test with {user}")

    def teardown(self):
        print("closing the browser")

obj_ref = Logintest()
obj_ref.setup()
obj_ref.run_test()
obj_ref.teardown()





