

from abc import ABC, abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def readfromexcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startbrowser(self):
        pass

    @abstractmethod
    def stopbrowser(self):
        pass

class TC1(Browser):
    def startbrowser(self):
        print("starting browser")
    def stopbrowser(self):
        print("stop the browser")

    def readfromexcel(self):
        print("reading from excel")

    def runTC(self):
        self.startbrowser()
        self.stopbrowser()
        self.readfromexcel()

tc1 = TC1()
tc1.runTC()