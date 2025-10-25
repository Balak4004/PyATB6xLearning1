'''
Check if the user can log in based on correct username and password.

I/p
username = "admin"
password = "1234"

O/p ✅ Login Successful
'''

username = input("enter username : ")
password = input("enter password : ")

if username == 'admin' and password == '1234':
    print("login successful")
else:
    print("login failed")