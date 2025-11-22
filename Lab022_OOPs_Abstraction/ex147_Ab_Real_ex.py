

from abc import ABC, abstractmethod

class BrowserManager(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stop command")

class Chromebrowser(BrowserManager):
    def start(self):
        print("we are starting the chrome")

tc1 = Chromebrowser()
tc1.start()
tc1.stop()
