
# double underscore __ = private

class Car:

    def __init__(self):

        self.password = "test123"
        #self.__password_secure = "pass123"

    def nany(self):
        self.__password_secure="1234"

object_ref = Car()
object_ref.nany()
print(object_ref.password)
print(object_ref._Car__password_secure)
