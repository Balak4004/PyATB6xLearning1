
class ExcelReader:
    @staticmethod
    def readexcelfile():
        print("Reading from Excel")

class DBConnection:
    @staticmethod
    def readMysqlfile():
        print("Reading from MySQL")

class TC1:
    def runTC(self):
        ExcelReader.readexcelfile()
        DBConnection.readMysqlfile()
        print("Hi")

class TC2:
    def runTC(self):
        ExcelReader.readexcelfile()
        DBConnection.readMysqlfile()
        print("Hello")

tc = TC1()
tc.runTC()
tc = TC2()
tc.runTC()