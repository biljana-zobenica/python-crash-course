class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []
 
    def list_flavors (self):
        print(f"\nWe have these flavors available: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

my_stand = IceCreamStand('Juicy')
my_stand.flavors = ['banana', 'kivi', 'apple', 'strawberries']

my_stand.describe_restaurant()
my_stand.list_flavors()
