

nums = [1,2,3,4,5,6]

def even_num(x):
    return x%2 == 0

even_numbers = list(filter(even_num,nums))
print(even_numbers)

list_student = [51,50,100]

keep_student = list(filter(lambda x:x>50,list_student))
print(keep_student)