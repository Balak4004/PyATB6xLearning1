

names = ["QA","Automation","","Test"]

non_empty = list(filter(lambda x: x!="",names))
print(non_empty)

non_empty1 = list(filter(None,names))
print(non_empty1)


def non_empty2(string):
    if string !="":
        return True
    return None

non_empty3 = list(filter(non_empty2,names))
print(non_empty3)