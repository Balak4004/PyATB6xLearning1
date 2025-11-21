


class Bank:

    def __init__(self,account_number,balance):
        self.balance = balance  #public
        self.__account_number = account_number

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance = self.balance + amount

    def show_account_number(self):
        self.__account_number = 123456123


hdfc = Bank(123456123,500)
hdfc.check_balance()
hdfc.deposit(200)
hdfc.check_balance()
hdfc.show_account_number()
print(hdfc._Bank__account_number)

