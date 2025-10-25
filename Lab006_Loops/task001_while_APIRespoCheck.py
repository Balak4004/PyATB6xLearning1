
'''An API sometimes fails due to network delays.
Write a program to retry the API call 3 times until the response code becomes 200.
If it still fails after 3 tries, print a failure message.
Hint: Use a while loop with a counter.
Hint: Use a while loop with a counter.
Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200 '''

count = 0

while count < 3:
    response = int(input("enter response code like 200, 300, 404, 500 etc:\n"))
    if response == 200:
        print("Attempt : ", count + 1, " Response : ", response)
        print("Test passed")
        break

    print("Attempt : ", count + 1, " Response : ", response)
    count = count + 1

else:
    print("Test failed")

