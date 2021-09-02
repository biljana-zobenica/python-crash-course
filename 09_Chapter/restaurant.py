class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The {self.name} restaurant is open!")

restaurant = Restaurant('Veggie', 'veggetarian')

restaurant.describe_restaurant()
restaurant.open_restaurant()