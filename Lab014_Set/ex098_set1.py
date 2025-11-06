

# set() = unordered collection and no duplicates

my_set = {1,2,3}
print(my_set)

my_set2 = {1,2,3,4,4,5,5}
print(my_set2)

list1 = [45.3,33,33,25]
set3 = set(list1)
print(set3)

t1 = ("test","for","test")
set4 = set(t1)
print(set4)

mixed = {1,True,"Man",3.5}
print(mixed)

# empty set
s1 = set()
print(type(s1))

for i in mixed:
    print(i)

mixed.add(4)
print(mixed)
mixed.remove(4)
print(mixed)