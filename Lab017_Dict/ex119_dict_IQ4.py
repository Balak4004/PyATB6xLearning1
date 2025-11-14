
# Remove duplicates values from dict

dict1 = {"a":1,"b":2,"c":1,"d":3}

unique_value = set()
result = {}

for key,value in dict1.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)

print(result)

