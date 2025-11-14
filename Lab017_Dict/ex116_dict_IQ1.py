

# Frequency of character in string (no of times character is present in string)


string = input("Enter the string e.g. automation\t")

char_count={}
for char in string:
    char_count[char] = char_count.get(char,0) + 1

print(char_count)
