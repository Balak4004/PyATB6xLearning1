

from collections import *
# COUNTER
user_input = input("enter a string\t")
count_char = Counter(user_input)
print(count_char)

# Namedtuple

info = namedtuple('info', ['name','age','ismarried'])
t = info('Pramod',34,True)

print(t.name)
print(t.age)
print(t.ismarried)