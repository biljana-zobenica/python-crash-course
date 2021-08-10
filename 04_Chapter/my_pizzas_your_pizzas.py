my_pizzas = ['vegeteriana', '4 cheese', 'margarita']
friend_pizzas = my_pizzas [ : ]

my_pizzas.append('pepperoni')
friend_pizzas.append('hawaiian')

print(f'My favorite pizzas are:')
for pizza in my_pizzas:
    print (pizza)

print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)