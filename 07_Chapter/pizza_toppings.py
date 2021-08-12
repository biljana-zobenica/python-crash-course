prompt = 'Enter your the toppings you would like on your pizza: '

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I will add {topping} to your pizza.")
    else:
        break
