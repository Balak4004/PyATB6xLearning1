

# Abstraction - Hide details and show only required

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name):
        self.name = name
        print(f"Dog name is {self.name}")

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog1 = Dog("PP")
dog1.sound()
