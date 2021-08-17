def make_car(manufacturer, model, **car_info):
    """Print a car info, stored in a dictionary."""
    print('Here are the main information about your car:')
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car ('subaru', 'outback', 
                color='blue', 
                tow_package=True)

print(car)
