car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

color = 'raspberry'
print("\nIs color == 'red'? I predict False.")
print(color == 'red')

fruit = 'raspberry'
print("\nIs fruit == 'raspberry'? I predict True.")
print(fruit == 'raspberry')

animal = 'dog'
print("\nIs animal == 'cat'? I predict False.")
print(animal == 'cat')

# test for equality
size = 'medium'
print("\nIs size == 'medium'? I predict True.")
print(size == 'medium')

# test for inequality
size = 'medium'
print("\nIs size != 'medium'? I predict False.")
print(size != 'medium')

# test using the lower() method
fruit = 'Raspberry'
print("\nIs fruit == 'raspberry'? I predict True.")
print(fruit.lower() == 'raspberry')

# numerical tests + using AND and OR keywords
size = 5
print(size == 5)
print(size == 7)
print(size > 2 and size < 7)
print(size > 3 or size == 5)
print(size <= 7)

# check whether an item IS or NOT IN a list
list = ['sun', 'sky', 'moon', 'mars', 'earth']
print(list)
print('sun' in list)
print('moon' not in list)
