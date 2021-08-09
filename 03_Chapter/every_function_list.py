# list of outdoor activities
# this file contains every function related to the list manipulation in the 3rd chapter
list = ['beach', 'mountain', 'cruise', 'camping']
print(f'Initial list: \n{list}')

list[2] = 'sailing'
print(f'\nChange the 3rd item: \n{list}')

list.append('trekking')
print(f'\nAdd an item at the end of the list: \n{list}')

list.insert(0, 'swimming')
print(f'\nAdd an item at the start of the list: \n{list}')

list.pop(0)
print(f'\nPop the first item: \n{list}')

list.remove('mountain')
print(f'\nRemove "mountain" from the list: \n{list}')

list.sort()
print(f'\nPermanently sorted list: \n{list}')
print(f'Check the list: \n{list}')

list.sort(reverse=True)
print(f'\nPermanently reverse sorted list: \n{list}')
print(f'Check the list: \n{list}')

print(f'\nTemporarily sorted list: \n{sorted(list)}')
print(f'Check the list: \n{list}')

list.reverse()
print(f'\nPermanently reverse list: \n{list}')
print(f'Check the list: \n{list}')

print(f'\nThis is the length of the list: {len(list)}')