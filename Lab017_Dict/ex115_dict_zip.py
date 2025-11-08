

keys = ("name","age","role","exp")
values = ("Aman",34,"SDET")

dict2 = dict(zip(keys,values))

print(dict2)

# merge two dict

dict3 = {"a":1,"b":2}
dict4 = {"c":3,"d":4}

merged_dict = dict3 | dict4
print(merged_dict)
print(merged_dict.get("a"))
