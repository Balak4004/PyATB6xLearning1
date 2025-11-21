

class Car:
    name = None
    make = None
    model = None

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print(f"Starting a car with name {self.name}")
        print(f"Starting a car with make {self.make}")
        print(f"Starting a car with model {self.model}")

tata = Car("Nexon","V8","2025")
tata.start_engine()

kia = Car("Seltos","V9","2024")
kia.start_engine()