def describe_city(city, country = 'Russia'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('Moscow')
describe_city('Rejkjavik', country = 'Ireland')
describe_city('Saint Petersburg')