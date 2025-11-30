

with open('testdata_1.txt','a') as file:
    content = file.write("\tBlueberry")
    print(content)

'''
with open('testdata_1.txt','a') as file:
    content = file.write("Blueberry")   # adds next to the last line
    content = file.write("\nBlueberry")     # adds to next line
    content = file.write("\tBlueberry")     # adds next to the last line with tab space
    print(content)

'''


