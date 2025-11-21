
from dotenv import load_dotenv
import os
class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirmation(self):
        load_dotenv()
        # to print env and input email and password
        #print("From env:", os.getenv("VWO_USERNAME"))
        #print("From env:", os.getenv("VWO_PASSWORD"))
        #print("From input:", self.email)
        #print("From input:", self.password)

        if self.email == os.getenv("VWO_USERNAME") and \
            self.password == os.getenv("VWO_PASSWORD"):
            print("Login successful")

        else:
            print("Login failed")

email = input("Enter the VWO login email\t")
password = input("Enter the VWO login password\t")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirmation()
