

shop_list = ["bread", "butter","paneer"]
shop_list[2] = "milk"
print(shop_list)


my_tuple = ("abc.com","cxx.com")
print(my_tuple)
my_list = list(my_tuple)
print(my_list)
my_list2 = tuple(my_list)
print(my_list2)


my_tuple = ("abc.com","cxx.com")
print(my_tuple)
my_list = list(my_tuple)
my_list.append("Jar")
my_list2 = tuple(my_list)
print(my_list2)

# create empty tuple and list
l = list()
print(l)

t = tuple()
print(t)


hero1 = ("Batman","Bruce")
hero2 = ("Wonder Woman","Diana")
new_tuple = (hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][0])
print(new_tuple[1][1])