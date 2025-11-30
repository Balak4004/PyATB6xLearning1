

try:
    with open('pramod.txt','r') as file:
        content = file.read()
        print(content)

except FileNotFoundError as fnferror:
    print(fnferror,"file not found error")
    