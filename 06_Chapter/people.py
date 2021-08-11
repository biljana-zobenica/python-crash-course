person_0 = {
    'first_name':'Eddie', 
    'last_name':'Jackson', 
    'age':'29', 
    'city':'Stockholm'
    }

person_1 = {
    'first_name':'Katty', 
    'last_name':'Thomas', 
    'age':'35', 
    'city':'Paris'
    }

person_2 = {
    'first_name':'Sam', 
    'last_name':'Polle', 
    'age':'36', 
    'city':'Lisbon'
    }

people = [person_0, person_1, person_2]

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city']
    print(f"{name} is {age} years old and live in the city of {city}.")