prompt = 'Please enter how old are you? '
prompt += ("\nEnter 'quit' when you are finished. ")

while True:
    age = int(input(prompt))
    if age == 'quit':
        break
    if age < 3:
        price = 'free'
    elif age < 12:
        price = '$10'
    elif age > 12:
        price = '$15'
    print(f'Your movie ticket is {price}.')