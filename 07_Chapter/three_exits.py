prompt = 'Enter your the toppings you would like on your pizza: '

# version 1 - use conditional test to stop the loop
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I will add {topping} to your pizza.")
    else:
        break

# version 2 - use an active variable to control how long the loop runs
active = True
while active:
    topping = input(prompt)
    print(f"I will add {topping} to your pizza.")
    if topping == 'quit':
        active = False

# version 3 - use a break statement to exit the loop
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"I will add {topping} to your pizza.")
    else:
        break