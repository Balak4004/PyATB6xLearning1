

class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirmation(self):
        if self.email == "test@gmail.com" and self.password == "Test@123":
            print("Login successful")
        else:
            print("Login failed")

email = input("Enter the VWO login email\t")
password = input("Enter the VWO login password\t")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirmation()
