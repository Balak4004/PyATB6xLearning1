
'''
In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches
True - why >  Strip and convert them into the lowercase = both of them are equal.
'''

expected_title = "Dashboard"

actual_title = input("enter the text : ").strip()

if expected_title.strip().lower() == actual_title.lower():
    print("test case passed ")
else:
    print("test case failed ")