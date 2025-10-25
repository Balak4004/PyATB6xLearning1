
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

statuscode = int(input("enter the status code : "))

if statuscode == 200:
    print("API request passed")
elif statuscode == 404:
    print("API Request failed")
else:
    print("enter valid statuscode")

