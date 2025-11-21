

class Testexample:

    def __init__(self):

        self.browser = "Chrome"
        self._config = "Stage"
        self.__api__key = "abc123"

    def show(self):
        print(self.browser)
        print(self._config)
        print(self.__api__key)

object_ref = Testexample()
object_ref.show()