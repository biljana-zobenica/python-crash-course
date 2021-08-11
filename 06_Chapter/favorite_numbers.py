# version 1
favorite_numbers = {
    'Nick':5, 
    'Bob':3, 
    'Mike':9,
    'Steve':12,
    'Spike':33,
    }

print(f"This is Nick's favorite number: {favorite_numbers['Nick']}.")
print(f"This is Bob's favorite number: {favorite_numbers['Bob']}.")
print(f"This is Mike's favorite number: {favorite_numbers['Mike']}.")
print(f"This is Steve's favorite number: {favorite_numbers['Steve']}.")
print(f"This is Spike's favorite number: {favorite_numbers['Spike']}.")

# version 2 -> multiple favorite numbers
favorite_numbers = {
    'Nick':[5, 7, 9] ,
    'Bob':[3, 1] ,
    'Mike':[9, 19, 119],
    'Steve':[12, 21],
    'Spike':[33, 22, 99],
    }

for person, numbers in favorite_numbers.items():
    print(f"These are {person.title()}'s favorite numbers:")
    for number in numbers:
        print(f"{number}")
