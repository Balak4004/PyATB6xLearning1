

test_result = ["PASS","FAIL","PASS","SKIP","FAIL"]

pass_test = list(filter(lambda x: x=="PASS",test_result))
print(pass_test)