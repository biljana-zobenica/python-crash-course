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

restaurant = Restaurant('Veggie', 'veggetarian')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(1234)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(316)
print(f"Number served: {restaurant.number_served}")