
# Pop -- Removes and return item at index (default index at last )


square = [1,4,9,16,25]
print(square.pop())
print(square)

print(square.pop(1))
print(square)

square.clear()
print(square)

# index = return index of first occurence of the element

numbers = [10,20,30,20,40]
print(numbers.index(20))
# count() - counts number of times element
print(numbers.count(20))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

# max() and min() and sum() for the list
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Slicing -
print(numbers)
print(numbers[1:4])     # from index of 1 to 3
print(numbers[-1])

print("apple" in numbers)
print(True in numbers)

# List creation and comprehension
l = list(range(1,5))
print(l)

# Nested list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])

# del() - delete element by index or whole list
print(numbers)
del numbers[0]
print(numbers)