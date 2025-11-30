

import os

print(os.getcwd())

full_path = os.path.join(os.getcwd(),"pramod.txt")
print(full_path)
fullpath1 = os.path.join(r'/Lab028_File_IO/pramod.txt')
print(fullpath1)

file = open(fullpath1,'r')
print(file.read())


file.close()