

# Abstraction - Hide details and show only required

from abc import ABC, abstractmethod

class Father(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Amit(Father):
    def loan(self):
        print("Giving 50k loan")

amit = Amit("Amit Sharma")
amit.loan()
