
'''
*
**
***
****
*****
'''

rows = int(input("enter rows for right angle triangle\t"))

for i in range(1,rows+1):
    for j in range(i):
        print("*",end="")
    print()