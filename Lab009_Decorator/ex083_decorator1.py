

def before_after_test(func):

    def wrapper():
        print("Before running the UI code")
        func()
        print("After running the UI code")

    return wrapper()

@before_after_test
def ui_test():
    print("I am running the UI test")