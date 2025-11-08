

dict1 = {
    "name":"Aman",
    "age":34,
    "role":"SDET",
    "exp":3
}

print(dict1)
print(dict1["age"])
print(dict1["role"])

dict1["role"] = "Manual Tester"
print(dict1)

del dict1["age"]
print(dict1)

for key,value in dict1.items():
    print(key,":",value)

print("age" in dict1)
print("role" in dict1)