# dictionary of rivers
rivers = {'danube':'serbia', 'volga':'russia', 'nile':'egypt'}

# print 3 sentences including key-value pairs
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# print 3 rivers which are mentioned
print(f"\nRivers mentioned are:")
for river in rivers.keys():
    print(river.title())

# print 3 countries which are mentioned
print(f"\nCountries mentioned are:")
for country in rivers.values():
    print(country.title())