'''Write a Function to Check Test Case Status
Problem:
Write a function check_status(status_code) that returns:
"PASS" if status_code = 200
"FAIL" if status_code = 400 or 500
"UNKNOWN" otherwise

Example Input & Output:
print(check_status(200))   # PASS
print(check_status(500))   # FAIL
print(check_status(302))   # UNKNOWN '''

def check_test_case_status():
    user_input = int(input("enter the test case status code\t"))
    match user_input:
        case 200:
            return "PASS"
        case 400 | 500:
            return "FAIL"
        case _:
            return "Unknown"

result = check_test_case_status()
print(result)
