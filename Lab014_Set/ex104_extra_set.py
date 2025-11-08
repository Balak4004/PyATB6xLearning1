
'''
# avoid one liner below code
squares = {x ** 2 for x in range(5)}
print(squares)

# Use below to square numbers
for x in range(5):
    squares.add(x**2)
print(squares)
'''
squares = set()
for x in range(5):
    squares.update([x**2])
print(squares)