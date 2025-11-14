
# palidrome string = when reversed then same as inital e.g. level


input_string = input("enter the string\t").strip().lower()

string2 = ""

for char in reversed(input_string):
    string2 = string2 + char

print(string2)

if input_string == string2:
    print(input_string, "is a palidrome")
else:
    print(input_string, "is not a palidrome")
