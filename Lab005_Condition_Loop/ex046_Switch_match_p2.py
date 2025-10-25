
print("Enter which Test you want to run")
# test type API, UI, Performance, Security
test_type = input("enter test type : ")

match test_type:
    case "API":
        print("we are running Postman Test case")
    case "UI":
        print("we are running selenium Test case")
    case "Performance":
        print("we are running performance test case")
    case "Security":
        print("we are running security test case")
    case _:
        print("Invalid type")

# convert match case into if else

test_type = input("enter test type : ")

if  test_type == "API":
    print("we are running Postman Test case")
elif test_type == "UI":
    print("we are running selenium Test case")
elif test_type == "Performance":
     print("we are running performance test case")
elif test_type == "Security":
    print("we are running security test case")
else:
    print("Invalid type")