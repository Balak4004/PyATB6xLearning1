
import time

def print_logs(func):

    def wrapper():
        print("start of the log")
        func()
        print("end of the log")
    return wrapper

def time_decorator(func):

    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time taken by function :", end_time - start_time)
    return wrapper


@time_decorator
@print_logs
def ui_test_1():
    print("Add function, time taken by the function 1")
    time.sleep(2)


@time_decorator
@print_logs
def ui_test_2():
    print("Add function, time taken by the function 2")
    time.sleep(5)


ui_test_1()
print("----------")
ui_test_2()