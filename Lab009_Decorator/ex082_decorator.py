

def add_security(func):

    def wrapper():
        print("1. Before the function is called")
        print("2.Add Helmet,goggle,license")
        func()
        print("3.After the function is called")
        print("4.Secure driving, leave all items")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")

@add_security
def drive_tvs_scooter():
    print("I am driving tvs scooter")
