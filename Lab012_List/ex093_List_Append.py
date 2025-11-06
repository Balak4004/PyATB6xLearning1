from Lab012_List.ex091_List1 import my_list

# append() - append object to the end of list


my_list = [1,2,3]

my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)

# extend() - append a new list
my_list.extend([7,8,10,9])
print(my_list)

# insert() -  add at particular index
my_list.insert(1,"Ja")
print(my_list)
print(len(my_list))

my_list.insert(0,0 )
print(my_list)

my_list[1] = "Amit"
print(my_list)

# remove() - remove specific element
my_list.remove('Amit')
print(my_list)

# copy() - copy same list
my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Ja")

print(my_list)
print(my_copy_list)

my_copy_list[1] = "Ja"
print(my_list)
print(my_copy_list)

my_list.remove("Ja") 

print(my_list)
print(my_copy_list) 
