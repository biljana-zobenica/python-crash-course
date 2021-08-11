# create a dictionary inside a dictionary
cities = {
    'moscow': {
        'country':'russia',
        'population': '12.5 million',
        'fact':'Moscow river flows through the city. There is the Kremlin fortress and the Red square in the city center.'
    },
    'dublin': {
        'country':'ireland',
        'population': '1 milion',
        'fact':'Liffey river flow through the city in which you can find the famous Temple bar.'
    },
    'stockholm': {
        'country':'sweden',
        'population': '1 milion',
        'fact':'It is the largest city in Scandinavia which hosts the annual Nobel Prize ceremonies.'
    },
}

# print out all the information related to each city
for city, details in cities.items():
    country = details['country'].title()
    population = details['population']
    fact = details['fact']
    print(f"\nThe city of {city.title()} is in {country}.")
    print(f"It has a population of around {population}.")
    print(f"{fact}")


