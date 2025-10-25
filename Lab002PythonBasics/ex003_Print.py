
print("Hello world!!!")

# To Open builtins.py file -- In your code, Ctrl+Click on the module (print)

#def print(self, *args, sep=' ', end='\n', file=None): # known special case of print

# *args, * means unlimited number of comma separated arguments
from datetime import date
print("Anil",123,"Ram",10.45,True,date(2024,1,1))

# sep = string inserted between values, default a space
from datetime import date
print("Anil",123,"Ram",10.45,True,date(2024,1,1), sep=" ")
print("Anil",123,"Ram",10.45,True,date(2024,1,1), sep=" | ")

# end = string appended after the last value, default a newline
print("Sam",777,"Toni",99.99,True,date(1900,1,1), sep=" ", end="\n")
print("Sam",777,"Toni",99.99,True,date(1900,1,1), sep=" | ")

print("Sam",777,"Toni",99.99,True,date(1900,1,1), sep=" ", end="__")
print("Sam",777,"Toni",99.99,True,date(1900,1,1), sep=" | ")

print("Sam",777,"Toni",99.99,True,date(1900,1,1), sep=" ", end=" ")
print("Sam",777,"Toni",99.99,True,date(1900,1,1), sep=" | ")

print("Jai",000,"Alex",1.01,True,date(9999,12,31), sep=" | ", end="_")