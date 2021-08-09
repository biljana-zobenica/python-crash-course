# list of 5 places in the world I'd like to visit
locations = ['Sydney', 'Tokyo', 'New York', 'Reykjavik', 'Agra']

# print the original list
print(f'Original list order: \n{locations}')

# print temporarily sorted list
print(f'Alphabetical list order: \n{sorted(locations)}')

# print original list, still in its original order
print(f'Original list order: \n{locations}')

# print temporarily sorted list in reverse alphabetical order
print(f'Reverse alphabetical list order: \n{sorted(locations, reverse=True)}')

# print original list, still in its original order
print(f'Original list order: \n{locations}')

# reverse the original list
locations.reverse()
print(f'Reversed original list order: \n{locations}')

# reverse the original list back to the original order
locations.reverse()
print(f'Original list order: \n{locations}')

# print permanently sorted list
locations.sort()
print(f'Permanently sorted list order: \n{locations}')

# print permanently reversed sorted list
locations.sort(reverse=True)
print(f'Permanently reversed sorted list order: \n{locations}')