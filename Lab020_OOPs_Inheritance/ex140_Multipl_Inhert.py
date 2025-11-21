

# Multiple Inherit -- subclass have more than one parent

class APIBase:

    def api_auth(self):
        print("authenticating API")

class DBBase:

    def db_connect(self):
        print("connecting to the DB")

class Testhybrid(APIBase,DBBase):
    def run(self):
        self.api_auth()
        self.db_connect()
        print("Running the Testcase")

t1 = Testhybrid()
t1.run()