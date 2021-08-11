pet_0 = {
    'type':'dog',
    'name':'rex',
    'color':'brown',
    'owner':'katty',
}

pet_1 = {
    'type':'cat',
    'name':'bobby',
    'color':'gray',
    'owner':'pete',
}

pet_2 = {
    'type':'horse',
    'name':'spirit',
    'color':'black',
    'owner':'bika',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['color']} {pet['type']} and is owned by {pet['owner'].title()}.")

