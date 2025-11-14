
# count vowel in a string vowels = a,e,i,o,u

'''
input_string = "hello, world!"

vowels = "aeiou"

vowels_count = 0
result = list()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count+1
        result.append(char)
print(vowels_count)
print(result)

input_string = "hello, world!"

consonent = "bcdfghjklmnpqrstvwxyz"

consonent_count = 0
result = list()

for char in input_string:
    if char in consonent:
        consonent_count = consonent_count+1
        result.append(char)
print(consonent_count)
print(result)

'''
input_string = "hello, world!"

vowels = "aeiou"
consonent = "bcdfghjklmnpqrstvwxyz"

vowels_count = 0
consonent_count = 0
result = list()
result2 = list()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count+1
        result.append(char)
    else:
        if char in consonent:
            consonent_count = consonent_count + 1
            result2.append(char)
print(vowels_count)
print(result)
print(consonent_count)
print(result2)