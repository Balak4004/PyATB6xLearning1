

# find first non-repeating character in string
# swiss ---> ans: w


print("swiss".count("s"))
print("swiss".count("w"))
print("swiss".count("i"))

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeating("swiss"))
print(first_non_repeating("annusinha"))
print(first_non_repeating("tttt"))
