# create a dictionary of people's favorite places
favorite_places = {
    'katty':['paris', 'moscow'],
    'sam':['london', 'lisbon', 'porto'],
    'pete':['helsinki', 'oslo', 'copenhagen'],
    'bika':['saint petersburg', 'stockholm', 'helsinki'],
}

# extract names of people by looping through the dictionary
for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    # extract favorite places of people by looping through the values in dictionary 
    # (since .title() can not be applied to a list nested for keys' values)
    for place in places:
        print(f"\t{place.title()}")
    