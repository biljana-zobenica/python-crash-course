foods = ('pizza', 'pasta', 'wraps', 'pancakes', 'salad')

print(f'Here are the restaurant offer:')
for food in foods:
    print (food.title())

#foods[0] = 'burger'
#TypeError: 'tuple' object does not support item assignment

updated_foods = ('cake', 'pasta', 'wraps', 'pancakes', 'salad')

print(f'\nHere is the updated restaurant offer:')
for food in updated_foods:
    print (food.title())